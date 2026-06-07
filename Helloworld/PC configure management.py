from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial;
                display: flex;
                flex-direction: column;
                align-items: center;
                background-color: #1a1a2e;
                color: white;
                padding: 20px;
            }
            h1 { margin-bottom: 30px; }
            .btn {
                width: 200px;
                padding: 15px;
                margin: 10px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
            }
            .green  { background-color: #4CAF50; color: white; }
            .red    { background-color: #f44336; color: white; }
            .blue   { background-color: #2196F3; color: white; }
            .orange { background-color: #FF9800; color: white; }
        </style>
    </head>
    <body>
        <h1>远程控制面板</h1>

        <a href="/open_video">
            <button class="btn green">▶️ 打开视频</button>
        </a>
        <a href="/close_video">
            <button class="btn red">⏹ 关闭视频</button>
        </a>
        <a href="/open_music">
            <button class="btn grey">🎵 打开音乐</button>
        </a>
        <a href="/sleep">
            <button class="btn blue">😴 睡眠</button>
        </a>
        <a href="/restart">
            <button class="btn orange">🔄 重启</button>
        </a>
        <a href="/shutdown">
            <button class="btn red">⏻ 关机</button>
        </a>
    </body>
    </html>
    '''


@app.route('/open_video')
def open_video():
    subprocess.run(['open', '/Users/jonny/Downloads/video/selfmovie.mov'])
    return '<a href="/">← 返回</a><p>✅ 视频已打开</p>'


@app.route('/close_video')
def close_video():
    subprocess.run(['pkill', 'QuickTime Player'])
    return '<a href="/">← 返回</a><p>✅ 视频已关闭</p>'


@app.route('/open_music')
def open_music():
    subprocess.run(['open', '/Users/jonny/Desktop/网易云音乐'])
    return '<a href="/">← 返回</a><p>✅ 音乐已打开</p>'


@app.route('/sleep')
def sleep():
    subprocess.run(['pmset', 'sleepnow'])
    return '<a href="/">← 返回</a><p>✅ 进入睡眠</p>'


@app.route('/restart')
def restart():
    subprocess.run(['sudo', 'shutdown', '-r', 'now'])
    return '<a href="/">← 返回</a><p>✅ 正在重启</p>'


@app.route('/shutdown')
def shutdown():
    subprocess.run(['sudo', 'shutdown', '-h', 'now'])
    return '<a href="/">← 返回</a><p>✅ 正在关机</p>'


app.run(host='0.0.0.0', port=5000)
