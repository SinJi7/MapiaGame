from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, rooms, join_room, leave_room, send
from flask import jsonify
import secrets

from flask_cors import CORS, cross_origin

from container import Container, make_container_start

#{RoomNumber: Container}
ROOM_CONTAINER:dict = {}

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = b"abcdefg"

socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == "__main__":
    print("secret")
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

# @app.route('/')
# def sessions():
#     return render_template('session.html')

@app.route('/token', methods=["GET", "POST"])
# parm: room_name user_name
def getToken():
    if "token" in session:
        print("중복입장")
        return jsonify(
            token=False
        )
    #front에서 중복 입장을 막는다
    #setting data
    room_name=request.args.get('room_name')
    user_name = request.args.get("user_name")
    rand_token = secrets.token_hex(nbytes=16)

    session["token"] = rand_token

    print(room_name)
    #room 생성
    if room_name in ROOM_CONTAINER:   
        #join room 
        ROOM_CONTAINER[room_name].addUser(rand_token, user_name)
        print(rand_token + " 방 입장")

        return jsonify(
            token=rand_token
        )
    else:
        #make room
        ROOM_CONTAINER[room_name] = make_container_start()
        ROOM_CONTAINER[room_name].addUser(rand_token, user_name)
        print(rand_token + " 방 생성")

        return jsonify(
            token=rand_token
        )

@socketio.on('addroom')
def join_room(data, methods=['GET', 'POST']):
    print("호출")

    room_name = str(data["room_name"])
    token = data["token"]
    session["token"] = token
    print(session)
    join_room(room_name)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('message')
#param: room_name, token, meesage, time
def handle_my_custom_event(json, methods=['GET', 'POST']):

    room_name = request.args.get("room_name"),
    data = {
        "room_name" : room_name,
        "token" : request.args.get("token"),
        "message" : request.args.get("message"),
        "time" : request.args.get("time")
    }

    print(room_name)
    print([i for i in ROOM_CONTAINER])
    ROOM_CONTAINER[room_name].sendMessage(send, data)

    print('received my event: ' + str(json))

    
    #socketio.emit()
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)

    #이벤트 처리 추가
    #socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, port=4000, debug=True)