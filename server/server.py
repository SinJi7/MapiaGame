from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit, join_room, close_room
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
    #socket.emit("test", "conected")

##############################################
#Staging Code
##############################################
#컨테이너 사용 추가하기


@socket.on('game_start')
def on_start_game(data): #Game 시간 동안 계속 유지된다
    print("================start_game====================")
    rq_room_name = data["room_name"]
    rq_user_name = data["user_name"]

    #reject contiditon
    #add token contiditon, next time
    if (
        ROOM_CONTAINER[rq_room_name].isPlayGame() or
        not ROOM_CONTAINER[rq_room_name].isOwner(rq_user_name) or
        ROOM_CONTAINER[rq_room_name].isRoomMemberCount()
       ):
        pass #return test 용도롤 조건 무시
    #Game Start
    ROOM_CONTAINER[rq_room_name].startGameSetting()
    ###########################################################
    #Game
    while True:
        if not ROOM_CONTAINER[rq_room_name].isPlayGame(): break

        ### 시간 변경 ###
        time_type = ROOM_CONTAINER[rq_room_name].change_time()
        if time_type:
            emit("time_update", {"time" : time_type, }, room=rq_room_name)

            target_dict_ls:list = ROOM_CONTAINER[rq_room_name].Target_Colleting(time_type) # dict
            #밤 -> 투표 (사형 대상)
            #투표 -> 밤 (사형 여부)
            #밤 -> 낮 (특수능력 사용 대상)
            #구현 미완료
            messages = ROOM_CONTAINER[rq_room_name].apply_target_to_game(time_type, target_dict_ls)
            ROOM_CONTAINER[rq_room_name].send_system_message("\n".join(messages))
        ################

        time.sleep(1)
        ROOM_CONTAINER[rq_room_name].doGame()
    close_room(f"{rq_room_name}_mapia") #열었던 경우 닫는다.
    close_room(f"{rq_room_name}_dead")
    ###########################################################

# type: data["type"],
# user_name: this.state.user_name,
# room_name: this.state.room_name,
# target_name : this.state.target
@socket.on('send_target')
def on_Target(data): #유저 필터링 미적용 타겟만 수집
    if "" == data["target_name"]:return
    room_name = data["room_name"]
    target_name = data["target_name"]
    user_name = data["user_name"]
    ROOM_CONTAINER[room_name].addTarget({user_name: target_name}) #user_name : target_name 형태로 수정 필요

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

    # message_handler({
    #     "room_name" : "room1",
    #     "user_name" : "room2",
    #     "message" : "room3"
    # })


# param : user_name, room_name
@socket.on("get_job")
def on_get_job(data):
    if ROOM_CONTAINER[data["room_name"]].isPlayGame():
        job_name = ROOM_CONTAINER[data["room_name"]].getJob(data["user_name"])
        emit("set_job", {"job_name" : job_name})

# use time : game start
# Action: if requester is mapia, join maipa romm
# param : user_name, room_name
@socket.on("join_mapia")
def on_join_mapia_handler(data):
    if ROOM_CONTAINER[data["room_name"]].isPlayGame():
        if ROOM_CONTAINER[data["user_name"]].isMapiaUser():
            join_room(f"{data['room_name']}_mapia")


# use time : client get death msg, call this
# Action: if requester is dead, join dead room
# param : user_name, room_name
@socket.on("join_dead")
def on_join_dead_handler(data):
    if ROOM_CONTAINER[data["room_name"]].isPlayGame():
        if ROOM_CONTAINER[data["user_name"]].isDeadUser():
            join_room(f"{data['room_name']}_dead")
            join_room(f"{data['room_name']}_mapia")


# use time : all time
# Action: send message.
#   Action case: not paly(afternoon, nigth, vote) / play
# param: room_name, user_name, message
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
    

