import mysql.connector
from classes.dbconfig import Connect

class Wedstrijd ():
    def __init__(self,match_ID=None,beginUur=None,eindUur=None,ploeg_1=None,ploeg_2=None,stadion_ID=None,score_ploeg_1=None,score_ploeg_2=None):
        self.match_ID=match_ID
        self.beginUur=beginUur
        self.eindUur=eindUur
        self.ploeg_1=ploeg_1
        self.ploeg_2=ploeg_2
        self.stadion_ID=stadion_ID
        self.score_ploeg_1=score_ploeg_1
        self.score_ploeg_2=score_ploeg_2
    
    def start ():
        pass
    
    def einde():
        pass
    
    def aflassen():
        pass
    
    def lijstWedstrijden ():
        pass
        