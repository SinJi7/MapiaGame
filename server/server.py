from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS

from container import Container, make_container_start
import asyncio

import time
import threading

# {RoomNumber: Container}
ROOM_CONTAINER: dict = {}

app = Flask(__name__, static_folder='../mapia_front/build/static')
app.config['SECRET_KEY'] = 'development key'
socket = SocketIO(app)
CORS(app)

# socketio = SocketIO(app, cors_allowed_origins="*")



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

@socket.on('game_start')
def on_start_game(data):
    rq_room_name = data["room_name"]
    rq_user_name = data["user_name"]
    #reject contiditon
    #add token contiditon, next time
    if (
        ROOM_CONTAINER[rq_room_name].isPalyGame() or
        not ROOM_CONTAINER[rq_room_name].isOwner(rq_user_name) or
        ROOM_CONTAINER[rq_room_name].isRoomMemberCount() #
       ):
        return
    #Game Start
    ROOM_CONTAINER[rq_room_name].startGameSetting() 

    while True:
        if not ROOM_CONTAINER[rq_room_name].isPalyGame(): break
        time.sleep(1)
        ROOM_CONTAINER[rq_room_name].doGame()  


@socket.on('join_room')
def join_handler(data):
    print("=============join_room=============")
    room_name = data["room_name"]
    join_room(room_name)

    #컨테이너 생성 or 입장
    if room_name not in ROOM_CONTAINER:
        ROOM_CONTAINER[room_name] = make_container_start(room_name, emit)
        ROOM_CONTAINER[room_name].addUser(data["user_name"])
    else:
        ROOM_CONTAINER[room_name].addUser(data["user_name"])

    message_handler({
        "room_name" : "room1",
        "user_name" : "room2",
        "message" : "room3"
    })

@socket.on('message')
#param: room_name, token, meesage, time
def message_handler(msg, methods=['GET', 'POST']):
    print("=============Message_On=============")
    #print(msg)
    #test code
    body = {
        "room_name" : msg["room_name"],
        "user_name" : msg["user_name"],
        "message" : msg["message"]
    }

    ROOM_CONTAINER[msg["room_name"]].sendMessage(body)
    #emit("message",  body, room=msg["room_name"])

    return

    print(room_name)
    print([i for i in ROOM_CONTAINER])
    

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
    

