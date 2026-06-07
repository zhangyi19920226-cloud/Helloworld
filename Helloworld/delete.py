import os
import subprocess

# 预先设定好文件位置
FILES = {
    '打开视频': '/Users/jonny/Downloads/video/selfmovie.mov',
    '打开音乐': '/Users/jonny/Desktop/网易云音乐'
}

command = input('请输入指令：')

if command in FILES:
    subprocess.run(['open', FILES[command]])  # Mac用open命令
else:
    print('没有找到对应的文件')
