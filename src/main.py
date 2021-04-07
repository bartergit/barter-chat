from flask import Flask, send_file, send_from_directory
from flask_socketio import SocketIO
import json

app = Flask(__name__, static_url_path='/file', static_folder='static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
messages = ['hello vue']
@app.route('/')
def index():
    return 'Indexx Page'

@app.route('/file')
def file():
    return send_from_directory('static', 'index.html')


@app.route('/hello')
def hello():
    return 'Hello, World'


@socketio.on('connect')
def handle_message():
    socketio.emit('update', json.dumps(messages))

@socketio.on('message')
def handle_message(message):
    messages.append(message["data"])
    print('received message: ' + str(message))
    socketio.emit('update', json.dumps(messages))


if __name__ == '__main__':
    socketio.run(app)
