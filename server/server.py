from flask import Flask, render_template
from flask_socketio import SocketIO

from flask_cors import CORS, cross_origin

app = Flask(__name__)
#app.config['SECRET_KEY'] = '비밀번호 설정'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('message')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    #socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, port=4000, debug=True)