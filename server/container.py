import threading

from mapia_core.Core import Game
import time

import asyncio
from flask import request

class Container(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""
    __RoomValid = True #방 유효
    
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
    def startGameSetting(self) -> bool:
        self.__Game = Game(self.__Users)

    def isPalyGame(self) -> bool:
        return self.__Game != None 

    def isOwner(self, name:str) -> bool:
        return self.__OWNER == name #임시 코드

    def isRoomMemberCount(self) -> bool:
        member_cnt = len([i for i in self.__Users])
        return True if (member_cnt == 6 or member_cnt ==  8 or member_cnt == 10) else False

    def endGame(self) -> dict:
        game_res = self.__Game.end_game()
        self.__Game = None
        return game_res

    def sendMessage(self, data) -> None:
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
    

