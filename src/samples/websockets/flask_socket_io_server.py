from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'include_help!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event', namespace='/my_namespace')
def test_message(message):
    emit('i said ', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/my_namespace')
def test_message(message):
    emit('i said ', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/my_namespace')
def test_connect():
    emit('i said ', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/my_namespace')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)