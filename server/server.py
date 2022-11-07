from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS

from container import Container, make_container_start

#{RoomNumber: Container}
ROOM_CONTAINER:dict = {}

app = Flask(__name__, static_folder='../mapia_front/build/static')
app.config['SECRET_KEY'] = 'development key'
socket = SocketIO(app)
CORS(app)

#socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def serve_static_index():
    return send_from_directory('../mapia_front/build', 'index.html')

#############################################
#test codes
#############################################
@socket.on('connect')
def on_connect():
    print('=============user_connected=============')
    socket.emit("test", "conected")

##############################################
#Staging Code
##############################################
#컨테이너 사용 추가하기
@socket.on('join_room')
def join_handler(data):
    print("=============join_room=============")
    room_name = data["room_name"]
    join_room(room_name)
    #컨테이너 생성 or 입장
    return 
    if room_name in ROOM_CONTAINER:
        ROOM_CONTAINER.append(make_container_start)
    else:
        pass


@socket.on('message')
#param: room_name, token, meesage, time
def message_handler(msg, methods=['GET', 'POST']):
    print("=============Message_On=============")
    print(msg)
    #test code
    body = {
        "room_name" : msg["room_name"],
        "user_name" : msg["user_name"],
        "message" : msg["message"]
    }
    emit("message",  body, room=msg["room_name"])
    return

    print(room_name)
    print([i for i in ROOM_CONTAINER])
    ROOM_CONTAINER[room_name].sendMessage(send, data)

    print('received my event: ' + str(json))
    
    #socketio.emit()
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)

    #이벤트 처리 추가
    #socketio.emit('my response', json, callback=messageReceived)

##############################################

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')



if __name__ == '__main__':
    socket.run(app, port=4000, debug=True)