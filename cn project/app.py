from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import pyautogui

app = Flask(__name__)
socket_ = SocketIO(app, async_mode='gevent', transport='udp')

@app.route('/')
def index():
    return render_template('index.html', sync_mode=socket_.async_mode)

@socket_.on('position')
def handle_position_message(message):
    pyautogui.move(message['data']['mouseX'], message['data']['mouseY'])
    print(message['data']['mouseX'], message['data']['mouseY'])

@socket_.on('clicked')
def handle_click_message(message):
    pyautogui.click()
    print(message['data']['mouseX'], message['data']['mouseY'])

@socket_.on('keyboard')
def handle_keyboard_message(message):
    pyautogui.press(message['data']['key'])
    print(message['data']['key'])

@socket_.on('connect')
def handle_connect():
    print("Socket connection made")

if __name__ == '__main__':
    socket_.run(app, host='192.168.83.35', debug=True, port=5002)
