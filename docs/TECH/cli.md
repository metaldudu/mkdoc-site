---
title: CLI
date: 2023-01-03
---

# CLI 

CLI（command-line interface，命令行界面），在命令行下面解决日常应用

---

## 常用工具

### 显示主机信息

 [neofetch](https://github.com/dylanaraps/neofetch)，以及 [pfetch](https://github.com/dylanaraps/pfetch)

### 显示天气

[ansiweather](https://github.com/fcambus/ansiweather)，或者使用 curl ：

`curl wttr.in/shijiazhuang`

### 显示时钟

[tty-clock](https://github.com/xorg62/tty-clock)，大字体、多种颜色

### 显示音乐波动

[cava](https://github.com/karlstav/cava)

### 词典

[cambrinary](https://github.com/xueyuanl/cambrinary) ，查询剑桥在线词典 

`cambrinary -w hello`

### RSS阅读器

newsboat [https://github.com/newsboat/newsboat](https://github.com/newsboat/newsboat)

## 多媒体

### 音乐播放

cmus [https://github.com/cmus/cmus](https://github.com/cmus/cmus)


## 音乐转换处理

参考[wiki](https://wiki.archlinux.org/title/CUE_Splitting) ，安装 shntool `yay -S shntool`

分割音频文件为flac ，注意 cue 文件编码为 UTF-8

`shnsplit -f CDImage.cue -t "%n - %t" -o flac CDImage.flac`

如果操作ape文件需要装 mac `yay -S mac`

## 文件重命名

### rename重命名

`rename`命令，archlinux的版本是C语言的，man查看例子：`rename .htm .html *.htm`

perl版本的rename 支持正则匹配，C版本不行

### 批量添加扩展名

`for f in *; do mv "$f" "$f.mp3"; done`

### 按照001/002这样排序：

`for f in *; do mv "$f" "00$f"; done`

### 把空格替换成.

`for f in *; do mv -i "$f" "${f// /.}"; done`


## 娱乐

俄罗斯方块： ctris