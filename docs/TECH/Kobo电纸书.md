---
title: kobo阅读器
type: 物
date: 2022-12-04
---

# Kobo电纸书

我手上的是 [Kobo Aura One](https://us.kobobooks.com/products/kobo-aura-one) ，无实体翻页键。使用原生系统，默认支持中文。没有安装 Koreader 的原因是麻烦

## 设置

### 激活

需要全局翻墙
### 传输

usb传输，使用 Calibre。使用 Calibre 的插件 KoboTouchExtended ，可以直接以 kepub 格式导出至  Kobo ，用户不需要干预，本地也不会保留 kepub格式

### kepub格式

kobo原生格式，用 Calibre 安装 KoboTouchExtended 插件（会自动传送 kepub 格式到设备本地并不会生成一份副本），可以避免 epub 格式无法调整行距、字体支持不全的问题，响应速度也快很多。

###  添加字体

在根目录 font 文件夹放字体。在用：

- LXGWWenKaiScreenR.ttf 鹭霞文楷的屏幕优化版
- FZYouSJW_507R.TTF 方正悠宋
- 京華老宋体

### 字典

内置字典需要全局翻墙激活

## 漫画

漫画太多不适合用 Calibre 管理，Kobo 支持 cbr/cbz 这种漫画格式，而且相当流畅（对比mobi），做好格式转换就可以。原则就是图片尽量无损。

CBconvert （ https://github.com/gen2brain/cbconvert ）支持转换 PDF/EPUB/MOBI 等格式到 CBZ ，支持图片增强和拉伸调整。实测的问题是 mobi 转换后没有封面和作者信息。拷贝：直接usb连接，拖到到根目录即可

传输：直接usb连接，拖到到根目录即可

### 如何自制cbz漫画

1.  找到在线漫画网站，比如一个竖屏拖动读取图片的站
2.  使用 ImageAssistant 这个浏览器插件，网址：[https://www.pullywood.com/ImageAssistant/](https://www.douban.com/link2/?url=https%3A%2F%2Fwww.pullywood.com%2FImageAssistant%2F&link2key=bf34d4695d) 可以批量下载当前网页的图片，支持筛选特定扩展名和大小的文件，并自动重命名下载等
3.  如果自己不浏览，可以用控制台脚本让页面自动滚动到页尾，浏览器 F12 - Console ，贴入下面命令：var scroll = setInterval(function(){ window.scrollBy(0,1000); }, 2000); 回车等着滚动完成，然后回到步骤2下载图片
4.  找到图片目录，用任何压缩工具压缩成 .zip 然后重命名为 .cbz
5.  这种方法无法显示作者等书籍信息
## 链接

- wiki https://en.wikipedia.org/wiki/Kobo_eReader
- 技巧 https://github.com/Megumi-B/Kobo_Tips