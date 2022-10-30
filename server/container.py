import threading

class Container(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""
    __RoomValid = True
    __GamePlay = False
    
    def __init__(self, RoomID, Users:list):
        """__init__ 메소드 안에서 threading.Thread를 init한다"""
        threading.Thread.__init__(self)
        #add Use Mapia-Core
        self.__Users = []
        self.__RoomID = RoomID
    
    def isRoomId(self, ID):
        return True if ID == self.__RoomID else False

    #False일 경우 객체 제거
    def isRoomValid(self):
        return self.__RoomValid

    def __doGame():
        pass #게임 진행 함수 여기에
        #reset 조건 필요

    #start 실행
    def run(self):
        while self.__RoomValid:
            if self.__GamePlay: self.__doGame()

            #채팅 부분 여기에 구현해야함


def make_container_start(RoomNumber, User):
    container = Container()
    container.start()
    return container
    

