import threading

from mapia_core.Core import Game
import time

import asyncio
from flask import request

class Container(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""
    __RoomValid = True #방 유효
    
    
    def __init__(self, name, func):
        self.__NAME:str = name
        """__init__ 메소드 안에서 threading.Thread를 init한다"""
        threading.Thread.__init__(self)
        self.__Game = None
        self.__Users = {} # key is name

        self.__emit = func
    
    # def isRoomId(self, ID):
    #     return True if ID == self.__RoomID else False

    def startGame(self, data):
        self.__Game = Game(self.__Users)

    def endGame(self):
        game_res = self.__Game.end_game()
        self.__Game = None
        return game_res
    def __isGamePlay(self): #Game 진행중 여부 
        return False if self.__Game == None else True

    def sendMessage(self, data):
        if self.__isGamePlay():
            if "aftermoon" == self.__Game.gameTime():
                pass #낮
            else:
                if self.__Game.isPlayerMapia():
                    pass #send message
        else:
            self.__emit("message", data, to=self.__NAME)
            
    #False일 경우 객체 제거

    def isRoomValid(self):
        return self.__RoomValid

    def __doGame(self):
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

    #start 실행
    def run(self):
        while self.__RoomValid:     
            #self.__emit("test", "SKdlfksfjsflsdfla", room=self.__NAME)
            if self.__isGamePlay(): self.__doGame()
            time.sleep(1)


def make_container_start(name, emit):
    container = Container(name, func=emit)
    container.start()
    return container
    

