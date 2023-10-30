# Firefox 浏览器

## 界面

使用 userChrome.css 定义紧凑布局：  https://github.com/Dook97/firefox-qutebrowser-userchrome


- **取消标题栏**：菜单栏右键 -- 定制 Firefox -- 左下角，取消标题栏勾选

### 优化配置

地址栏输入 `about:config` 进入高级首选项，搜索

- browser.tabs.closeTabByDblclick 打开双击关闭tab
- mousewheel.default.delta_multiplier_y` -- 把默认值100改成65，滚轮速度变慢一些
- browser.download.alwaysOpenPanel = false -- 关闭下载弹出框

## 自定义搜索引擎

- 从 [Mycroft Project: Search Engine Plugins](https://mycroftproject.com/) 网站添加

## 扩展

- uBlock Origin - 广告过滤
- uBlacklist - 屏蔽特定网站搜索结果
- [CopyTabTitleUrl](https://addons.mozilla.org/en-US/firefox/addon/copytabtitleurl/) - 拷贝markdown格式的URL
- Proxy SwitchyOmega - 代理切换
- [Violentmonkey](https://addons.mozilla.org/zh-CN/firefox/addon/violentmonkey/) - 脚本，开启 webdav 同步，配置坚果云
- [Dark Mode](https://mybrowseraddon.com/dark-mode.html) - 相对好用的暗色模式切换

