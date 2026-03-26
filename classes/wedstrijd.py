import mysql.connector
from classes.dbconfig import Connect

class Wedstrijd ():
    def __init__(self,match_ID=None,begin_uur=None,eind_uur=None,ploeg_1=None,ploeg_2=None,stadion_ID=None,score_ploeg_1=None,score_ploeg_2=None):
        self.match_ID=match_ID
        self.begin_uur=begin_uur
        self.eind_uur=eind_uur
        self.ploeg_1=ploeg_1
        self.ploeg_2=ploeg_2
        self.stadion_ID=stadion_ID
        self.score_ploeg_1=score_ploeg_1
        self.score_ploeg_2=score_ploeg_2
        
    def __repr__(self):
        return f'wedstijd (match_ID={self.match_ID},begin_uur={self.begin_uur}, eind_uur={self.eind_uur}, ploeg_1={self.ploeg_1}, ploeg_2={self.ploeg_2},stadion_ID={self.stadion_ID},score_ploeg_1={self.score_ploeg_1},score_ploeg_2={self.score_ploeg_2})'
    
    def start ():
        pass
    
    def einde():
        pass
    
    def aflassen():
        pass
    
    def lijstMatchen (the_db):
        sqltxt = "Select stadion_ID,stadion_naam,stadion_zetels FROM klanten stadion_ID"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()
        return [Wedstrijd(*row) for row in result]
        