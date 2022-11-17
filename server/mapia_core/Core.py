from datetime import datetime, timedelta
from random import randint

import time


#역할은?
class Game:
  __game_players: list = []
  __game_time: dict 
  #initializer area

  #parm 유저 식별자(이름)
  def __init__(self, playerDict:dict):
    playerIds = [i for i in playerDict] 
    rand_jobs :list = self.__makeRandomJob(len(playerIds))
    self.__set_game_time("afternoon") #{ "time" : "aftermoon", "next" : datetime.now() + timedelta(seconds=90)}

    for idx in range(len(playerIds)):
      self.__game_players.append({"name": playerIds[idx], "job_name": rand_jobs[idx], "live": True})

    #self.jobls = [Player(playerIds[i], rand_jobs[i]) for i in range(len(playerIds))]

  #player count
  #return: random job list [mapia... citizen]
  #parm: playerCount(player count), mapia_count: default 2
  def __makeRandomJob(self, playerCount:int, mapia_count:int = 2):
    base_job_ls = ["mapia" for _ in range(mapia_count)] + ["citizen" for _ in range(6 - 8 + playerCount)]
    rand_job_ls = [base_job_ls.pop(randint(0, i-1)) for i in range(len(base_job_ls), 0, -1)]
    return rand_job_ls # [mapia... citizen]

  #param: find_user_name
  #return: user_dict
  def __findUser(self, find_user_name) -> dict:
    #if can't find user, return this
    base = {"name": "null", "job_name": "citizen", "live": False}

    for user_dict in self.__game_players:
      if user_dict["name"] == find_user_name:
        base = user_dict

    return base

  #getter
  def getUserLive(self) -> list:
    return [{"name" : player_dict["name"], "live" : player_dict["live"]} for player_dict in self.__game_players]

  def getTime(self):
    return self.__game_time["time"]
    
  def getPlayer(self, id):
    for player in self.__game_players:
      if id == player: return player.__getId()
    return None
    
  def getDeathPlayer(self, id):
    for player in self.__game_players:
      if id == player: return player.__getId()
    return None
    
  def isPlayerMapia(self, user_name):
    user_obj:dict = self.__findUser(user_name)
    return "mapia" == user_obj["job_name"]

  def getPlayerJob(self, user_name):
    user_obj = self.__findUser(user_name)
    return user_obj["job_name"]

  def isDeadUser(self, user_name):
    return 

  #game control
  def get_player_ablity_parm(self, id):
    pass
  def use_player_ablity(self, id):
    pass
  def kill_player(self):
    pass

  def isVoteTime(self):
    if self.__game_time["time"] == "aftermoon" and self.__game_time["next"] <= datetime.now():
      return True

  def end_game(self):
    if len([player for player in self.__game_players if player.getlive() and player.getJob()]) == 0:
      return True

  #############################################
  #private game control
  #############################################

  #setter
  def __set_game_time(self, time_type:str) -> None:
    #time_type_seconds:dict = {"afternoon": 120,"night": 60,"vote": 20}
    time_type_seconds:dict = {"afternoon": 25,"night": 25,"vote": 25}
    next_second = time_type_seconds[time_type]

    self.__game_time = {
      "time":time_type, 
      "next" : datetime.now() + timedelta(seconds=next_second)
    }

  ##############################################
  #Staging Code
  ##############################################

  #function: time check, change time
  def change_time(self):
    def get_next(now_time):
      TIME_LS = ["afternoon","vote","night"]
      now_idx = TIME_LS.index(now_time)
      return TIME_LS[(now_idx + 1) % 3]
    
    #if now time is change time, call setter
    if datetime.now() >= self.__game_time["next"]:

      next_time:str = get_next(self.__game_time["time"])

      self.__set_game_time(time_type=next_time)
      return next_time
    else: 
      return False
  ##############################################


#미사용 코드
#########################################################3
#직업, 생존여부를 저장한다.
class Player:
  __name: str
  __live: bool = True

  def __init__(self, name, job_name):
    self.__name = name
    self.__player_job = Job(job_name)

  def getJob(self):
    return self.__player_job
  def get_name(self):
    return self.__name
  def getlive(self):
    return self.__live

class Job:
  #initializer area
  def __init__(self, job_name):
    self.__name = job_name
    self.__ability = self.__setability(job_name)
    pass

  def get_name(self):
    return self.__name

  def __setability(self, name):
    def mapia(game: Game, player_id, get_parm=False):
      if get_parm: return ["kill_player"]
    def doctor(game: Game, player_id, get_parm=False):
      if get_parm: return ["heal_player"]
    def police(game: Game, player_id, get_parm=False):
      if get_parm: return ["check_player"]
    def citizen(game, get_parm=False):
      if get_parm: return []

      res_ability = citizen

      for func in [mapia, doctor, police]:
        if func.__name__ == name:
          res_ability = func
