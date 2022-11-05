import threading

from mapia_core.Core import Game

class Container(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""
    __RoomValid = True #방 유효
    
    def __init__(self):
        """__init__ 메소드 안에서 threading.Thread를 init한다"""
        threading.Thread.__init__(self)
        self.__Game = None
        self.__Users = {} #token : nickname
    
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

    def sendMessage(self, func, data):
        USERNAME = self.__Users[data["token"]]
        MESSAGE = data["message"]
        TIME = data["TIME"]

        send_data = {
            "user_name" : USERNAME,
            "message" : MESSAGE,
            "time" : TIME
        }

        if self.__isGamePlay():
            if "aftermoon" == self.__Game.gameTime():
                pass #낮
            else:
                if self.__Game.isPlayerMapia():
                    pass #send message
        else:
            func(send_data, data["room_name"])
            
    #False일 경우 객체 제거

    def isRoomValid(self):
        return self.__RoomValid

    def __doGame(self):
        pass #게임 진행 함수 여기에
        #reset 조건 필요

    def addUser(self, user_token, name):
        self.__Users[user_token] = name

    def delUser(self, user_token):
        self.__User.pop(user_token)
    
    def isInUser(self, user_token):
        return True if user_token in self.__Users else False

    #start 실행
    def run(self):
        while self.__RoomValid:
            if self.__isGamePlay(): self.__doGame()


def make_container_start():
    container = Container()
    container.start()
    return container
    

