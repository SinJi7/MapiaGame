import threading

#from mapia-core.Core import Game

class Container(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""
    __RoomValid = True
    __GamePlay = False
    
    def __init__(self):
        """__init__ 메소드 안에서 threading.Thread를 init한다"""
        threading.Thread.__init__(self)
        #add Use Mapia-Core
        self.__Users = {} #token : nickname
    
    # def isRoomId(self, ID):
    #     return True if ID == self.__RoomID else False

    def sendMessage(self, func, data):
        """
        if 게임중:
            if 낮:
            elif 밤:
                if 시민
                if 마피아
        elif 게임중이 아님
        """

        for data["token"] in self.__Users:
            func({'data': data, 'username': token}, data["room_name"])
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
            if self.__GamePlay: self.__doGame()

            #채팅 부분 여기에 구현해야함


def make_container_start():
    container = Container()
    container.start()
    return container
    

