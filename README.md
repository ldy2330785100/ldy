# <img src="https://ldy2330785100.github.io/ldy/Picture/profile.jpg" width="25" align="center"> 旅冬亦的个人网站

欢迎访问我的个人网站！这是一个展示个人信息、作品集与动态交互的静态网页项目。  
网站支持深色/浅色主题切换、自定义字体、实时运行时长统计、作品展示和精选视频，并包含完整的设置面板与更新日志。

<div>
  <a href="https://github.com/ldy2330785100/ldy/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  </a>
  <a href="https://ldy2330785100.github.io/ldy/">
    <img src="https://img.shields.io/badge/website-live-brightgreen" alt="Website">
  </a>
  <br>
  <a href="https://github.com/ldy2330785100/ldy/stargazers">
    <img src="https://img.shields.io/github/stars/ldy2330785100/ldy" alt="GitHub stars">
  </a>
  <a href="https://github.com/ldy2330785100/ldy/commits/main">
    <img src="https://img.shields.io/github/last-commit/ldy2330785100/ldy" alt="GitHub last commit">
  </a>
  <a href="https://github.com/ldy2330785100/ldy/releases">
    <img src="https://img.shields.io/github/v/release/ldy2330785100/ldy" alt="GitHub release">
  </a>
  <a href="https://github.com/ldy2330785100/ldy/releases">
    <img src="https://img.shields.io/github/release-date/ldy2330785100/ldy" alt="Release date">
  </a>
  <a href="https://github.com/ldy2330785100/ldy">
    <img src="https://img.shields.io/github/repo-size/ldy2330785100/ldy" alt="Repo size">
  </a>
  <a href="https://github.com/ldy2330785100/ldy/commits/main">
    <img src="https://img.shields.io/github/commit-activity/m/ldy2330785100/ldy" alt="Commit activity">
  </a>
  <a href="https://github.com/ldy2330785100/ldy">
    <img src="https://img.shields.io/badge/Maintenance-Active-brightgreen" alt="Maintenance">
  </a>
</div>

## 🌟 核心功能

### 主页
- **响应式设计**：圆角卡片与毛玻璃效果
- **动态头像**：悬停动画
- **个人信息展示**：姓名、个性签名
- **作品展示**：项目卡片包含网站 Logo、技术栈、GitHub 链接和在线体验链接
- **精选视频**：播放器优先加载，播放、点赞、投币、收藏、评论等统计异步获取，支持横竖屏比例自适应
- **联系方式**：邮箱、电话、GitHub 仓库、个人网站链接
- **社交媒体链接**：GitHub、微信、QQ、Bilibili、抖音、快手
- **顶栏**：支持双击回顶，可按需切换常驻或自动隐藏

### 设置面板
- **外观模式**：自动、浅色、深色
- **主题动画**：深浅色切换支持从点击位置扩散的过渡动画
- **字体选择**：系统默认、MiSans、小米兰亭、HarmonyOS Sans、OPPO Sans、汉仪文黑、汉仪旗黑、iOS Sans
- **性能设置**：动画效果（节流/平衡/优雅）、视觉效果（模糊/标配/通透）、顶栏状态、振动反馈
- **状态信息**：当前时间、最后更新时间、网站运行时长
- **刷新按钮**：强制刷新网页
- **更新日志**：跳转查看更新日志 `changelog.html`

### 交互体验
- 按钮与链接点击支持振动反馈
- 设置页面弹出/关闭动画
- 卡片淡入滚动动画
- 顶栏自动显示/隐藏
- 页面内容无需滚动时，顶栏自动切换为常驻

## 🎨 设计特色

1. **视觉风格**
   - Material 3 Expressive 毛玻璃效果（`backdrop-filter`）
   - 半透明背景与细边框，增强层次感
   - 圆角卡片与圆角矩形按钮
   - 主题色（`#0066BB`），深色模式（`#D9E9F1`）

2. **主题系统**
   - 支持手动切换
   - 切换后保存至 `localStorage`，随cookie生效
   - 深浅色切换支持扩散动画

3. **字体系统**
   - 支持自定义字体
   - 切换前预加载字体，避免显示闪变

4. **响应式设计**
   - 移动端优先的媒体查询
   - 按钮反馈与长按手势

## 🛠 技术栈

- **HTML5**：语义化标签
- **CSS3**：
  - Flexbox / Grid 布局
  - CSS 变量与主题切换
  - 过渡与关键帧动画
  - 自定义字体（`@font-face`）
  - 毛玻璃效果（`backdrop-filter`）
- **JavaScript**：
  - 动态主题切换与本地存储
  - 实时时间与运行时长计时
  - 内联数据渲染作品和视频，本地运行与服务器运行行为匹配
  - B 站 API 获取视频统计，支持超时控制与降级处理
  - 视频比例自适应
  - 帧率统计与滚动性能优化（`requestAnimationFrame`）

## 📱 手机端支持

本网页拟打包为 **Android APK**，提供两种类型：

- **在线版 Online**：~~网页映射至软件，内容与网站同步更新~~（已弃用）
- **离线版 Offline**：打包网页源文件至软件，可离线查看，更新需重新下载（已立项）

## 🔗 源码

- 👉 [前往下载](https://github.com/ldy2330785100/ldy/releases/)

## 📝 更新日志

- [ChangeLog](https://ldy2330785100.github.io/ldy/changelog.html)

## ⚠️ 声明

1. **项目性质**：本项目为个人技术练习与作品展示，非商业用途，不代表任何官方立场。
2. **版权与许可**：
   - **代码**：本项目采用 **[CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)** 开源。
   - **字体**：项目中引用的字体文件受版权保护，**不包含在 CC-BY-NC-SA-4.0 许可范围内**。
   - **头像**：头像为原创，未经允许禁止商用；如需个人使用请告知作者。
3. **责任限制**：作者不对因使用本项目代码或访问网站内容导致的任何损失承担责任。
4. **隐私说明**：本网站为纯静态页面，不收集任何用户隐私数据，所有设置仅保存在浏览器本地。

## 🙏 特别鸣谢

- [GitHub](https://github.com) 提供仓库与 Pages 托管服务
- [DeepSeek](https://chat.deepseek.com) 提供技术建议与代码优化
- [RikkaHub](https://rikka-ai.com)提供高效的开发环境

## 💬 讨论群聊

- [Telegram](https://t.me/WT_Permission)

---

<div align="center">
  &copy; 2026 旅冬亦 版权所有
</div>