from datetime import datetime, timedelta
from random import randint

import time


#역할은?
class Game:
  game_players: list
  game_time: dict = { "time" : "aftermoon", "next" : datetime.now() + timedelta(seconds=90)}
  #initializer area

  #parm 유저 식별자(이름)
  def __init__(self, playerIds:list): 
    randjobs :list = self.__makeRandomJob(len(playerIds))

    self.jobls = [Player(playerIds[i], randjobs[i]) for i in range(len(playerIds))]

  def __makeRandomJob(self, playerCount:int):
    game_players = ["mapia" for _ in range(2)] + ["citizen" for _ in range(6 - 8 + playerCount)]
    return [self.jobls.pop(randint(0, i-1)) for i in range(len(self.jobls), 0, -1)] #

  #getter
  def getTime(self):
    return self.game_time["time"]
    
  def getPlayer(self, id):
    for player in self.game_players:
      if id == player: return player.__getId()
    return None
  def getDeathPlayer(self, id):
    for player in self.game_players:
      if id == player: return player.__getId()
    return None
  def isPlayerMapia(self, token):
    #no implemented
    return False

  #game control
  def get_player_ablity_parm(self, id):
    pass
  def use_player_ablity(self, id):
    pass
  def kill_player(self):
    pass
  def isVoteTime(self):
    if self.game_time["time"] == "aftermoon" and self.game_time["next"] <= datetime.now():
      return True
  def death_check(self, id, yes, no):
    return True
  def end_game(self):
    if len([player for player in self.game_players if player.getlive() and player.getJob()]) == 0:
      return True

  #private game control
  def __change_time(self):
    if self.game_time["time"] == "night":
      self.game_time["time"] = "aftermoon"
      self.game_time["next"] = datetime.now() + timedelta(seconds=90)
    elif self.game_time["time"] == "aftermoon":
      self.game_time["time"] = "night"
      self.game_time["next"] = datetime.now() + timedelta(seconds=30)


#직업, 생존여부를 저장한다.
class Player:
  __name: str
  __live: bool = True

  def __init__(self, name, job_name):
    self.__name = name
    self.__player_job = Job(job_name)

  def getJob(self):
    return self.__player_job
  def getId(self):
    pass
  def getlive(self):
    return self.__live

from pygments.styles import get_all_styles

class Job:
  #initializer area
  def __init__(self, name):
    self.name = name
    self.ability = self.__setability(name)
    pass
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
