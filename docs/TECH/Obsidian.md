---
tags: 软件技巧

---

# Obsidian

## 简介

- [[我的笔记术进化史]]
- markdown文本
- [[双向链接]]，用双括号实现

## 安装配置

无法下载插件和主题，需要翻墙。 使用插件：https://github.com/juqkai/obsidian-proxy-github

### 快捷键

ctrl+E 预览模式
ctrl+K 插入链接
ctrl+O 快速切换笔记
ctrl+shift+上 左右分屏显示

### callout

https://help.obsidian.md/How+to/Use+callouts

默认支持多种列表图标，比如：info / todo / tip / check / help / fail / error / bug  / example / warning / quote

### 主题

- https://github.com/chrisgrieser/shimmering-focus 极简紧凑主题
- https://github.com/jdanielmourao/obsidian-sanctum


### 插件

无法更新插件，使用代理： `obsidian --proxy-server="http://127.0.0.1:9087"
`
- https://github.com/yucai100/obsidian-proxy-github 更新插件代理，可能已经失效
- advanced table 参考： [Obsidian 高级表格插件 (Advanced Tables) 的安装与使用 | ReadingHere](https://www.readinghere.com/blog/obsidian-advanced-tables-plugin/)
- dataview 参考： https://cyddgh.github.io/post/202103152106/
- https://github.com/mgmeyers/obsidian-style-settings 调整主题
- https://github.com/nothingislost/obsidian-hover-editor 浮窗编辑

### 搭配工具

[TabCopy](https://chrome.google.com/webstore/detail/tabcopy/micdllihgoppmejpecmkilggmaagfdmb) 拷贝网址为特定格式

### dataview 插件


#### 最近修改
```dataview
	LIST WHERE file.mtime >= date(today) - dur(10 day) sort file.mtime desc limit (5)
```

读书记录展示：

- https://github.com/zhaohongxuan/obsidian-weread-plugin/wiki/%E4%BD%BF%E7%94%A8Dataview%E8%BF%9B%E8%A1%8C%E4%B9%A6%E7%B1%8D%E7%AE%A1%E7%90%86
- https://minimal.guide/cards 卡片视图！

#### 显示图书封面的网址，但目前有些无法显示

```dataview
	table "![\|120](https://dou.img.lithub.cc/book/" + doubanid +".jpg)" as Cover, author as Author from "Reading/all books" AND #r/reading 
	sort file.name ASC
```

## 笔记方法

### MOC

MOC（Map Of Content）类似TOC，但可以用正常笔记形式，把其他笔记嵌入进来，用笔记串联笔记。MOC可以极大提升[[双向链接]]系统的效率。

就像卡片笔的盒子，MOC就是当作盒子的笔记，把一定主题的卡片集合在一起。

### 日记

参考：[How I Use the Daily Notes Plugin in Obsidian.md: A Comprehensive Guide – The Buccaneer's Bounty](https://thebuccaneersbounty.wordpress.com/2022/01/05/how-i-use-the-daily-notes-plugin-a-comprehensive-guide/)

日记的内容可以统计。

### 读书笔记

- 读书笔记的例子，作者和书籍分开 https://jamierubin.net/blog-series/practically-paperless-with-obsidian/

## 帖子和链接

- 中文官方论坛 https://github.com/obsidianzh/forum/discussions
- 中文教程 https://publish.obsidian.md/chinesehelp
- [回归 Obsidian 的纯与真，写给普通人的入门指南 - 少数派](https://sspai.com/post/72697)
- https://sspai.com/post/62414
- https://sspai.com/post/60802
- https://zhuanlan.zhihu.com/p/149969933
- https://einverne.github.io/post/2021/01/my-method-to-take-notes-using-zettelkasten-and-obsidian.html
- https://github.com/kmaasrud/awesome-obsidian

---

## 别人的公开笔记

- oldwinterの数字花园  https://notes.oldwinter.top/ 
- https://notes.singee.me/
- 管理电影的例子： https://www.zhihu.com/question/20548322/answer/2733002613
- 个人图书馆的例子： https://zhuanlan.zhihu.com/p/614286218