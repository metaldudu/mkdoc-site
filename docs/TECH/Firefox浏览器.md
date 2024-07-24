# Firefox 浏览器

## 界面

- 官方指南： https://www.reddit.com/r/firefox/wiki/userchrome/
- 布局：
	- github主题搜一个喜欢的 https://github.com/topics/userchrome
	- 精简功能的主题 https://github.com/Dook97/firefox-qutebrowser-userchrome
	- 在用的一个 https://github.com/dannycolin/fx-compact-mode
- **取消标题栏**：菜单栏右键 -- 定制 Firefox -- 左下角，取消标题栏勾选

### 优化配置

地址栏输入 `about:config` 进入高级首选项，搜索

- browser.tabs.closeTabByDblclick 打开双击关闭tab
- mousewheel.default.delta_multiplier_y` -- 把默认值100改成65，滚轮速度变慢一些
- browser.download.alwaysOpenPanel = false -- 关闭下载弹出框

## 自定义搜索引擎

- 从 [Mycroft Project: Search Engine Plugins](https://mycroftproject.com/) 网站添加

## 扩展

- uBlock Origin - 广告过滤，简中环境无法安装
	- 此扩展会导致 google drive 变成离线模式，关闭即可
- uBlacklist - 屏蔽特定网站搜索结果
- [Dark Reader](https://darkreader.org/) - 相对好用的暗色模式切换
- [CopyTabTitleUrl](https://addons.mozilla.org/en-US/firefox/addon/copytabtitleurl/) - 拷贝markdown格式的URL
- Proxy SwitchyOmega - 代理切换
- [Violentmonkey](https://addons.mozilla.org/zh-CN/firefox/addon/violentmonkey/) - 油猴脚本支持，可以用 webdav 同步配置文件，比如坚果云


## 其他技巧

- 对于某些不允许复制的网站，可以打开阅读模式（ctrl + alt + r）
- 