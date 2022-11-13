import threading

from mapia_core.Core import Game
import time

import asyncio
from flask import request

class Container(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""
    __RoomValid = True #방 유효

    #오너 결정 추가 필요
    def __init__(self, name, func):
        #"""__init__ 메소드 안에서 threading.Thread를 init한다"""
        threading.Thread.__init__(self)
        
        #User Data
        self.__OWNER:str = ""
        self.__NAME:str = name
        self.__Users = {} # key is name
        
        self.__Game = None #Use Gaem class

        self.__emit = func 

        #임시데이터들 초기화 함수 필요
        self.__target_collect = []
    
    # def isRoomId(self, ID):
    #     return True if ID == self.__RoomID else False

    #tmp data 관리
    #게임 영역에서 작동한다
    
    def isTarget_CollectComplete(self) -> bool:
        return len(self.__target_collect) == len(self.__Users)

    def Target_clear(self) -> None:
        self.__target_collect.clear()
    
    ###########
    # 호출시 현재 타겟을 수집 하고 반환한다
    # sever.py send_target에 의존하고 있다.
    def Target_Colleting(self, type) -> list: #sever.py에서 호출해야 함
        self.__emit("get_target", {"type": type}, room=self.__NAME)
        time.sleep(1)
        body = {
        "room_name" : self.__NAME,
        "user_name" : "admin",
        "message" : "투표 결과를 수집합니다"
        }
        self.__emit("message", {"type": type}, room=self.__NAME)
        #수정 필요 영역
        time.sleep(5) #send_target이 완료되기 위해서
        # isTarget_CollectComplete(self)
        # datatiem 이용 5초 동안 대기 가능하게 제작
        ################################
        res_targets = self.__target_collect[:]
        self.Target_clear()
        return res_targets

    def addTarget(self, name):
        self.__target_collect.append(name)    
    
    def change_time():
        return Game.change_time()
        
    def apply_target_to_game(self, type, targets) -> list:
        res_messages = []
        return res_messages

    ####################################
    #게임 시작 / 종료
    def startGameSetting(self) -> bool:
        self.__Game = Game(self.__Users)

    def endGame(self) -> dict:
        game_res = self.__Game.end_game()
        self.__Game = None
        return game_res
    #####################################

    def isPalyGame(self) -> bool:
        return self.__Game != None 

    def isOwner(self, name:str) -> bool:
        return self.__OWNER == name #임시 코드

    def isRoomMemberCount(self) -> bool:
        member_cnt = len([i for i in self.__Users])
        return True if (member_cnt == 6 or member_cnt ==  8 or member_cnt == 10) else False


    def send_system_message(self, message):
        body = {
            "room_name": self.__NAME,
            "user_name": "admin",
            "message": message
        }
        self.__emit("message", body, to=self.__NAME)

    def sendMessage(self, data) -> None: #sever.py 에서 호출 해야함
        if self.__isGamePlay():
            if "aftermoon" == self.__Game.gameTime():
                pass #낮
            else:
                if self.__Game.isPlayerMapia():
                    pass #send message
        else:
            self.__emit("message", data, to=self.__NAME)
            
    #False일 경우 객체 제거

    def isRoomValid(self) -> bool:
        return self.__RoomValid

    def doGame(self):
        #낮, 밤 변경
        pass #게임 진행 함수 여기에
        #reset 조건 필요


    def __userFilter(self, *args):
        result_user_ls = []

        for user_naem_key in self.__Users:
            #user name is default key
            user = {}
            user["user_name"] = user_naem_key
            #if args is in UserKeys, add User dict 
            for get_key in args:
                if get_key in self.__Users[user_naem_key]:
                    user[get_key] = self.__Users[user_naem_key][get_key]

            result_user_ls.append(user)

        return result_user_ls


    def addUser(self, name):
        self.__Users[name] = {"info": "chat", "token":"no implement"}

        self.__emit("user_update", {"users": self.__userFilter("info")}, room=self.__NAME)


    def delUser(self, user_token):
        self.__User.pop(user_token)
    
    def isInUser(self, user_token):
        return True if user_token in self.__Users else False

    #Not Use
    def run(self):
        while self.__RoomValid:     
            #self.__emit("test", "SKdlfksfjsflsdfla", room=self.__NAME)
            if self.__isGamePlay(): self.doGame()
            time.sleep(1)

        


def make_container_start(name, emit):
    container = Container(name, func=emit)
    #container.start()
    return container
    

