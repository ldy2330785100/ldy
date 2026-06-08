import os
import subprocess
import re
import json
import sys

def run_cmd(cmd, capture_output=True):
    result = subprocess.run(cmd, shell=True, capture_output=capture_output, text=True)
    if result.returncode != 0:
        print(f"命令执行失败: {cmd}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip() if capture_output else None

def get_latest_release_tag():
    output = run_cmd("gh release list --limit 1 --json tagName --jq '.[0].tagName'")
    if output:
        return output
    return None

def get_commits_between(start_tag, end="HEAD"):
    if not start_tag:
        first_commit = run_cmd("git rev-list --max-parents=0 HEAD")
        start = first_commit
    else:
        start = start_tag
    cmd = f"git log {start}..{end} --format=%s"
    messages = run_cmd(cmd).split("\n")
    return [msg.strip() for msg in messages if msg.strip()]

def determine_bump_type(commit_messages):
    major_keywords = ["BREAKING CHANGE:", "major:"]
    minor_keywords = ["feat:", "feature:", "minor:"]
    for msg in commit_messages:
        if any(kw in msg for kw in major_keywords):
            return "major"
    for msg in commit_messages:
        if any(kw in msg for kw in minor_keywords):
            return "minor"
    return "patch"

def bump_version(version, bump_type):
    # 版本号格式 v1.2.3
    match = re.match(r"v(\d+)\.(\d+)\.(\d+)", version)
    if not match:
        raise ValueError(f"Invalid version format: {version}")
    major, minor, patch = map(int, match.groups())
    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    else:  # patch
        patch += 1
    return f"v{major}.{minor}.{patch}"

def tag_exists(tag):
    cmd = f"git tag --list {tag}"
    output = run_cmd(cmd)
    return output == tag

def create_tag(tag):
    run_cmd(f"git tag {tag}", capture_output=False)
    run_cmd(f"git push origin {tag}", capture_output=False)
    print(f"创建新标签: {tag}")

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN 环境变量未设置")
        sys.exit(1)

    run_cmd(f"echo {token} | gh auth login --with-token")

    latest_release_tag = get_latest_release_tag()
    if latest_release_tag:
        print(f"上一个有效 Release 标签: {latest_release_tag}")
        base_tag = latest_release_tag
    else:
        print("没有找到任何 Release，将视为全新项目")
        base_tag = None

    commit_messages = get_commits_between(base_tag)
    if not commit_messages:
        print("没有新的 commit，无需发布")
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write("new_tag=\n")
        sys.exit(0)

    bump_type = determine_bump_type(commit_messages)
    print(f"版本升级类型: {bump_type}")

    if base_tag is None:
        new_tag = "v0.0.0"
        new_tag = bump_version(new_tag, bump_type)
    else:
        new_tag = bump_version(base_tag, bump_type)
    print(f"新版本标签: {new_tag}")

    if tag_exists(new_tag):
        print(f"标签 {new_tag} 已存在（空标签），将直接使用")
    else:
        print(f"标签 {new_tag} 不存在，创建新标签")
        create_tag(new_tag)

    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"new_tag={new_tag}\n")

if __name__ == "__main__":
    main()