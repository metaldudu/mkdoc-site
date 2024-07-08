---
title: Arch linux 笔记
date: 2022-12-04
---

# Arch linux 笔记

## 系统安装

按照wiki走一遍，不行就再来一遍。有可能踩坑：

- 和win10共享ESP分区的话，100Mb 不够用，而且win10更新会导致 grub 错误。建议扩大 ESP 分区
- 命令行状态下要装好网络包
- 自动挂载移动硬盘和U盘，安装 `ntfs-3g udevil` ，同时当前用户要增加权限。解决弹出提示输入密码的问题：[链接](https://askubuntu.com/questions/552503/stop-asking-for-authentication-to-mount-usb-stick)


## 网络

查询本机ip： `$curl ipinfo.io`

## 系统更新

### mirrors

编辑：`/etc/pacman.d/mirrorlist`

生成地址： [https://archlinux.org/mirrorlist/](https://archlinux.org/mirrorlist/)

### pacman错误

invalid pgp key错误解决 : `$ sudo pacman-key --refresh-keys`

pacman -Syu 升级系统
pacman -Syy 同步软件列表
pacman -Scc 清理软件包
pacman -S xxx 安装
pacman -Ss xxx 查询
pacman -R xxx 卸载
pacman -Rs xxx 卸载包以及依赖包
pacman -Rns xxx 删除包且删除配置文件
pacman -Qs xxx 查询已安装包
pacman -Rs $(sudo pacman -Qdtq) 删除孤儿包

### yay

`yay -Ps`    现状展示
`yay -Qu` 查看待升级的包
`yay -Sc`    清理

## xfce4设置

### 显示

使用2k显示器开缩放会很大，可以调整 Settings - Appearance - Fonts - DPI 到130左右

### 音频

蓝牙支持：

sudo pacman -S bluez bluez-utils blueman pulseaudio-bluetooth

sudo systemctl restart bluetooth.service

### 主题

使用暗色主题：`pacman -S arc-gtk-theme` ，图标选择： papirus-icon-theme 。所有的图标在：`/usr/share/icons/` 修改文件夹颜色 [papirus-folders](https://github.com/PapirusDevelopmentTeam/papirus-folders)

### 壁纸

壁纸位置在：~/.local/share/xfce4/backdrops/

### 面板

- 声音：安装 alsa-utils 和  pulseaudio。安装　`xfce4-pulseaudio-plugin` ，面板添加音量图标
- 任务栏靠左后，可以设置时钟显示，参考[这里]() ，自定义时间格式为： %H%n⋅⋅%n%M
- 系统栏图标大小不合适，参考[这里](https://bbs.archlinux.org/viewtopic.php?id=222292)
- 【故障】桌面窗口标题栏消失，无法拖动和改变大小，或者面板消失。解决方法：`xfwm4 --replace &`
- 

### 快捷键

- 窗口靠边：win+方向键
- 隐藏所有窗口：win+D
- 启动器，使用  [Ulauncher](https://github.com/Ulauncher/) ：win+~
- 截图，使用 Flameshot ：`flameshot gui > win+3`
- 解决 xfce4-terminal 填充空隙问题 [url](https://forum.xfce.org/viewtopic.php?pid=66277#p66277)

### 字体

参考这个： https://wiki.archlinuxcn.org/wiki/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE/%E4%B8%AD%E6%96%87

查看中文字体： `fc-list :lang=zh` 可以看到字体名，便于配置软件 
`fc-cache -fv` 刷新字体显示

```
sudo pacman -S ttf-dejavu wqy-microhei noto-fonts-emoji
```

不要安装谷歌东亚字体，会造成混乱：`noto-fonts-cjk` 安装思源黑体和宋体：

```
sudo pacman -S adobe-source-han-sans-cn-fonts  adobe-source-han-serif-cn-fonts  
```

- [简体中文等距更纱黑体+Nerd图标字体库](https://github.com/laishulu/Sarasa-Mono-SC-Nerd) 适合终端中英文混排使用  `yay -S nerd-fonts-sarasa-mono`
- 编程字体：[Fira Code](https://github.com/tonsky/FiraCode)

自己安装的字体放到 `~/.local/share/fonts`

适合阅读和电纸书的字体

- [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)（免费）选择 霞鹜文楷屏幕阅读版
- 方正屏显雅宋（付费，屏幕显示优化） FZPingXYSK.TTF
- 方正宋刻本秀楷简体 
- 筑紫明朝体，适合繁体字
- 京華老宋体

## 输入法

选择 fcitx5 和 rime ，使用：

- 四叶草拼音方案 https://github.com/fkxxyz/rime-cloverpinyin 不喜欢四叶草图标，可以修改 `~.local/share/fcitx5/rime/build/clover.schema.yaml` 文件里的 🍀 为其他字符，比如 🐼
- 自己修改了一份皮肤 [metaldudu/fcitx5-simple-white-theme](https://github.com/metaldudu/fcitx5-simple-white-theme)

比起默认的拼音更适合简体中文用户。一些快捷键：

- F4 设置菜单
- shift+空格 切换全角/半角
- ctrl+shift+3 切换emoji

## 软件及配置

### 代理

terminal使用代理

```
alias setproxy="export ALL_PROXY=socks5://127.0.0.1:1080"
alias unsetproxy="unset ALL_PROXY"
aliass ip="curl ipinfo.io"
```

### 启动器

[Ulauncher](https://ulauncher.io/)，简单高效。无论用哪个平台都应该又一款趁手的启动器。

支持使用 `goldendict $1` 来调用 goldendict 查词

### 文件管理

压缩 `pacman -S thunar-archive-plugin`  ，文件搜索：catfish 。访问共享，安装 `gvfs-smb`

Thunar 支持 custom actions ，参考[这里](https://www.reddit.com/r/xfce/comments/9649y4/nice_thunar_trick/)，可以在右键菜单添加一个“复制当前目录”

`echo -n "%F" | xclip -selection c`

比如用 GIMP 打开图片，添加： `gimp %f`
### 编辑器

Typora 收费后，直接全部用 Obsidian 解决笔记问题，markdown无敌。Code-OSS 编辑多个文件，单个文件用系统自带的 mousepad 打开。LibreOffice 或者用腾讯在线文档对付 msoffice 格式。

`sudo pacman -S libreoffice-still libreoffice-still-zh-cn`

### 外语学习

GoldenDict （有分支强化版本 [GoldenDict-ng](https://github.com/xiaoyifang/goldendict-ng)） 和 [[anki]] 装好每天都用

### 图片

编辑器用 GIMP，用惯了也还好。看图用 ristretto ，看漫画可以用 MComix 或 Foliate。截图用火焰截图 [Flameshot](https://github.com/lupoDharkael/flameshot) ，截图可以绑定快捷键到 `flameshot gui` 

延时6秒截图命令： `flameshot gui -d 6000`

### 影音

- MPV 主力播放。 VLC 可以看网络直播流，也适合播放整个文件夹，VLC可以批量转换音频视频，也可以订阅 podcast
- 音乐播放用 Audacious ，专辑管理用 [AQuod Libet](https://quodlibet.readthedocs.io/en/latest/)，需要编辑音乐信息装一个 Kid3。听在线音乐可以用 [Listen 1 音乐播放器](https://listen1.github.io/listen1/) 。
- 录音用  Audacity

#### mpv显示两个字幕

mpv some-video.mp4 --sub-file=sub1.srt --sub-file=sub2.srt --secondary-sid=2

在线工具合并两个字幕： https://easypronunciation.com/zh/merge-two-subtitle-files-online

mpv调整字幕大小

- shitft + g : to increase font size
- shitft + f : to decrease font size

官方快捷键： https://mpv.io/manual/master/

### 电子书

Calibre 安装好，导入书库。需要编辑epub 可以安装 Sigil，有打包电子书的需要装 pandoc ，安装 `yay -S pandoc-bin`

pdf浏览就装 Evince ，图形化的PDF剪裁工具 [krop](http://arminstraub.com/software/krop) 

#### pdftk

- 提取pdf信息 `pdftk 1.pdf dump_data output out.txt`
- 更新pdf信息 `pdftk 1.pdf update_info out.txt output new.pdf`
- 合并 `pdftk file1.pdf file2.pdf cat output output.pdf`

#### qpdf

- 拆分pdf  `qpdf --empty --pages infile.pdf 1-5 -- outfile.pdf`
- 拆分pdf的简单方法是用内置pdf浏览器打印到pdf文件！

### 浏览器

Firefox 主力可同步，Chrome 备用

#### 浏览器无法打开telegram 链接

`~/.local/share/applications` 找到 userapp-Telegram Desktop-xxxx.desktop ,在文件的最后添加一行：

`MimeType=application/x-xdg-protocol-tg;x-scheme-handler/tg;`

### RSS

[Liferea](https://lzone.de/liferea/) 信息摄入主要来源
 
### 下载

wget  / [lux-dl](https://github.com/iawia002/lux) / youtube-dl / qbittorrent  / [AriaNg](https://github.com/mayswind/AriaNg)


### 即时通讯

微信，统信 UOS 版有小问题，也可以chrome，用下面命令开一个独立窗口

`google-chrome-stable --new-window --app=https://wx.qq.com`

### 网盘



坚果云打开后白屏，按照[这里的提示](https://blog.zhullyb.top/2021/10/02/nutstore-guide-on-archlinux-kde/)，执行：

`sudo sed -i 's|webui.enable=true|webui.enable=false|' /opt/nutstore/conf/nutstore.properties`

2022.5 坚果云会默认安装轻应用，会自动关联md格式，已放弃。改用 Syncthing

### Syncthing

- 安装 syncthing 或 syncthing-gtk ，多个PC和手机同步文件夹
- 加入服务： `sudo systemctl enable syncthing@laodu.service`
- 启动服务： `sudo systemctl start syncthing@laodu.service`

### SSH and git

- 安装 openssh git
- 创建本地ssh key：` ssh-keygen -t rsa -C "youremail@example.com"`
- 复制 `~.ssh/id_rsa.pub` 内容到github-Account settings-SSH Keys，Title随意
- 配置git，参考：https://www.runoob.com/w3cnote/git-guide.html

## 其他问题

#### 环境变量

编辑 `~/.bashrc`，加入 `export PATH=$PATH:/somepath`

#### 电源休眠

编辑： /etc/systemd/logind.conf 加入以下两行，实现笔记本合盖挂起系统：

    HandleLidSwitch=suspend
    HandleLidSwitchExternalPower=suspend

然后执行：`systemctl restart systemd-logind`


使用xfce后默认锁屏是xfce4-screensaver，调用 xflock4，黑屏无提示。卸载掉 xfce4-screensaver ，安装 

`sudo pacman -S light-locker`
`yay light-locker-settings`

然后在 设置>配置编辑器>xfce4-session>general>LockCommand 加入

`light-locker-command --lock`

则可以使用 ctrl+alt +L 锁定，返回 lightdm登录界面。可以安装 lightdm-gtk-greeter-settings 进一步美化登录界面。

#### 错误

!!! 问题，关闭笔记本盖子再打开，屏幕会出现

#: ../src/xfpm-power.c:436
msgid ""
"None of the screen lock tools ran successfully, the screen will not be locked.\n"
"Do you still want to continue to suspend the system?"
msgstr "嘿，所有锁屏工具都不能正常运行呢，所以我就无法锁定屏幕啦。\n您想继续挂起系统么？"

edit `/usr/bin/xflock4`

#### Telegram无法输入中文

- 编辑 ~/.local/share/applications/telegramdesktop.desktop
- 在命令部分前面加入 `env QT_IM_MODULE=fcitx`
- 重新打开菜单快捷方式
## 结语

奥卡姆剃刀原则说：如无必要、勿增实体。够用好用，还要怎样？
