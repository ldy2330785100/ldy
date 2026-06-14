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
- **动态头像**：悬停时放大动画
- **个人信息展示**：姓名、个性签名
- **作品展示**：从 `data.json` 动态加载项目卡片，包含技术栈、GitHub链接和在线体验链接
- **精选视频**：自动获取Bilibili播放量、弹幕数、点赞数和评论数（测试中）
- **联系方式**：GitHub仓库、个人网站链接
- **社交媒体链接**：GitHub、微信、QQ、Bilibili、抖音、快手
- **顶栏**：支持双击回顶

### 设置面板
- **外观模式**：自动、浅色、深色，手动切换且不受系统深色模式覆盖
- **字体选择**：系统默认、MiSans、小米兰亭、HarmonyOS Sans、OPPO Sans、汉仪文黑、汉仪旗黑
- **状态信息**：
  - 当前时间
  - 最后更新时间
  - 网站运行时长
- **刷新页面**：刷新当前页面
- **更新日志**：跳转到更新日志 `changelog.html`

### 交互体验
- 所有按钮均带有按压缩放反馈（`pressed` 效果）
- 设置面板弹出时背景模糊并锁定页面滚动，关闭后恢复
- 弹出/关闭动画使用 `ease-out` 缓动，过渡自然流畅
- 卡片淡入滚动动画
- 顶栏平滑显示/隐藏

## 🎨 设计特色

1. **视觉风格**
   - Material 3 Expressive 毛玻璃效果（`backdrop-filter: blur(16px)`）
   - 半透明背景与细白边框，增强层次感
   - 圆角卡片（12px）与按钮（圆角矩形）
   - 主题色深蓝（`#00668B`），深色模式下为（`#D9E9F1`）

2. **主题系统**
   - 支持用户切换，不依赖浏览器
   - 切换后保存至 `localStorage`，下次访问恢复

3. **字体系统**
   - 支持多种自定义字体
   - 字体切换实时生效

4. **响应式设计**
   - 移动端优先的媒体查询
   - 触摸按钮反馈

## 🛠 技术栈

- **HTML5**：语义化标签，无障碍支持
- **CSS3**：
  - Flexbox / Grid 布局
  - CSS 变量与主题切换
  - 过渡与关键帧动画
  - 自定义字体（`@font-face`）
  - 毛玻璃效果（`backdrop-filter`）
- **JavaScript**：
  - 动态主题切换与本地存储
  - 实时时间与运行时长计时器
  - 设置面板动画与滚动锁定
  - Fetch 获取 `data.json` 动态渲染作品和视频
  - B站API调用获取视频统计数据
  - 滚动性能优化（`requestAnimationFrame` 节流）

## 📱 手机端支持

本网页拟打包为 **Android APK**，提供两种类型：

- **在线版 Online**：网页映射至软件，内容与网站同步更新（已弃用）
- **离线版 Offline**：打包网页源文件至软件，可离线查看，更新需重新下载（已立项）

## 🔗 源码

- 👉 [前往下载](https://github.com/ldy2330785100/ldy/releases/)

## 📝 更新日志

- [ChangeLog](https://ldy2330785100.github.io/ldy/changelog.html)

## ⚠️ 声明

1. **项目性质**：本项目为个人技术练习与作品展示，非商业用途，不代表任何官方立场。
2. **版权与许可**：
   - **代码**：本项目采用 **[MIT License](https://opensource.org/licenses/MIT)** 开源。
   - **字体**：项目中引用的字体文件受版权保护，**不包含在 MIT 许可范围内**。
   - **头像**：头像为原创，未经允许禁止商用；如需个人使用请告知作者。
3. **责任限制**：作者不对因使用本项目代码或访问网站内容导致的任何损失承担责任。
4. **隐私说明**：本网站为纯静态页面，不收集任何用户隐私数据，所有设置仅保存在浏览器本地。

## 🙏 特别鸣谢

- [GitHub](https://github.com) 提供仓库与 Pages 托管服务
- https://qianwen.aliyun.com & https://chat.deepseek.com 提供技术建议与代码优化
- [Font Awesome](https://fontawesome.com) 提供图标库

---

<div align="center">
  &copy; 2026 旅冬亦 版权所有
</div>