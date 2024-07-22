# 中文歌曲节拍数

中文歌每分钟节拍数统计，找到适合自己跑步步频的单曲

🎧 🏃 💦 🎵

---

## 100 - 140

- 100 - 郝云-突然想到理想这个词
- 100 - 苏阳乐队 - 贤良
- 102 - 蔡依林-說愛你
- 103 - S.H.E-痛快
- 106 - 孙燕姿 - 绿光
- 110 - G.E.M.-夜空中最亮的星
- 120 - 阿肆-我在人民广场吃炸鸡版
- 120 - 黑豹-无地自容
- 121 - 再见杰克 - 痛苦的信仰
- 124 - 给我一点爱--面孔乐队
- 124 - 张震岳-再见
- 126 - 崔健一无所有
- 129 - 王菲-梦中人
- 130 - 脆莓-十七岁少女金色心
- 132 - 朴树 - New Boy
- 141 - 杨乃文 - 静止

## 150 - 170

- 149 - 金色年华, 无限伤感 - 刺猬乐队
- 150 - 李宗盛 - 山丘
- 150 - 赵雷-南方姑娘
- 154 - 易燃易爆炸
- 156 - 五月天-借问众神明
- 166 - 孙燕姿 - 天黑黑
- 168 - 朴树-平凡之路
- 168 - 孙燕姿 - 直来直往
- 168 - 赵雷-我们的时光
- 170 - 苏打绿 - 一起喔喔

## 180👍

- 179 - 李荣浩 老街
- 180 - 蔡依林 - 骑士精神
- 180 - 莫文蔚 - 打起手鼓唱起歌
- 180 - 痛仰乐队 - 为你唱首歌 
- 180 - 许巍 - 蓝莲花
- 180 - 张震岳 - 思念是一种病

## 180+

- 182 - 田震 - 风雨彩虹铿锵玫瑰
- 182 - 赵雷-成都
- 184 - 许巍-第三极
- 186 - 林志炫 - 单身情歌
- 186 - 麦田守望者 在路上
- 187 - 许巍-像风一样自由
- 191 - 曹芳-遇见我


## tools

检测工具：bpm-tools [http://www.pogo.org.uk/~mark/bpm-tools/](http://www.pogo.org.uk/~mark/bpm-tools/)

```
#!/bin/bash
MUSICDIR="/home/laodu/tmp/180bpm/"
cd "$MUSICDIR"

find -type f -iname "*.mp3" | while read FILE
do
    BPM=`bpm-tag -n "$FILE" 2>&1 > /dev/null | grep BPM | awk '{print $(NF-1)}'` #105.587
    echo $FILE $BPM
    id3v2 --TBPM $BPM "$FILE"
done

```

english songs links:

- https://www.ladysouthpaw.com/180-bpm-running-songs

### 180 bpm songs :

├── 50 cent - In Da Club - 90bpm.mp3
├── Alabama Shakes - Hold On (KONK Session) - 89bpm.mp3
├── Gorillaz - 19-2000 - 89bpm.mp3
├── Judy Is a Punk (2016 Remaster) - 91bpm.mp3
├── Katy Perry - Roar - 90bpm.mp3
├── Metric - Gold Guns Girls - 90bpm.mp3
├── Red Hot Chili Peppers - Someone- 91bpm.mp3
├── Rihanna - Diamonds - 92bpm.mp3
├── Taylor Swift - Our Song - 89bpm.mp3
├── The Vapors  - Turning Japanese - 89bpm.mp3
├── Van Morrison - Bright Side of the Road - 88bpm.mp3
└── Van Morrison - For Mr. Thomas - 90bpm.mp3
