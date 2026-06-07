from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/open_video')
def open_video():
    subprocess.run(['open', '/Users/jonny/Downloads/video/selfmovie.mov'])
    return 'ok'


@app.route('/close_video')
def close_video():
    subprocess.run(['pkill', 'QuickTime Player'])
    return 'ok'


@app.route('/sleep')
def sleep():
    subprocess.run(['pmset', 'sleepnow'])
    return 'ok'


@app.route('/restart')
def restart():
    subprocess.run(['sudo', 'shutdown', '-r', 'now'])
    return 'ok'


@app.route('/shutdown')
def shutdown():
    subprocess.run(['sudo', 'shutdown', '-h', 'now'])
    return 'ok'


app.run(host='0.0.0.0', port=5001)
