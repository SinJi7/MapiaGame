from flask import Flask, render_template, request, session
from flask_socketio import SocketIO
from flask import jsonify
import secrets

from flask_cors import CORS, cross_origin

from container import Container, make_container_start

#{RoomNumber: Container}
ROOM_CONTAINER:dict = {}

app = Flask(__name__)
CORS(app)
#app.config['SECRET_KEY'] = '비밀번호 설정'
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == "__main__":
    print("secret")
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

# @app.route('/')
# def sessions():
#     return render_template('session.html')

@app.route('/token', methods=["GET", "POST"])
# parm room_number name
def getToken():
    #False 조건
    print(session)
    if ("name" not in request.args) and ("room_number" not in request.args):
        return jsonify(
            token=False
        )
    if "username" in session:
        print("not give token")
        return jsonify(
            token=False
        )
    #setting data
    room_number=request.args.get('room_number')
    rand_token = secrets.token_hex(nbytes=16)
    name = request.args.get("name")

    session['username'] = rand_token #make Session
    print(session)

    #room 생성
    if room_number in ROOM_CONTAINER:

        ROOM_CONTAINER[room_number].addUser("rand_token", name)
        print(rand_token + " 방 입장")
        return jsonify(
            token=rand_token
        )
    else:
        ROOM_CONTAINER[room_number] = make_container_start()
        ROOM_CONTAINER[room_number].addUser("rand_token", name)

        print(rand_token + " 방 생성")
        return jsonify(
            token=rand_token
        )

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('message')
def handle_my_custom_event(json, methods=['GET', 'POST']):

    room_number = request.args.get("room_number")
    data = request.args.get("data")
    ROOM_CONTAINER[room_number].sendMessage(socketio.emit, data)

    print('received my event: ' + str(json))

    
    #socketio.emit()
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)

    #이벤트 처리 추가
    #socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, port=4000, debug=True)