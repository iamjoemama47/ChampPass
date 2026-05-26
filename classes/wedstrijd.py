import mysql.connector
from classes.dbconfig import Connect

class Wedstrijd ():
    def __init__(self, wedstrijd_ID=None,begin_Uur=None,eind_Uur=None,ploeg_Naam1=None,logo_Img1=None,ploeg_Naam2=None,logo_Img2=None,stadion_Naam=None,score_ploeg_1=None,score_ploeg_2=None):
        self.wedstrijd_ID=wedstrijd_ID
        self.begin_Uur=begin_Uur
        self.eind_Uur=eind_Uur
        self.ploeg_Naam1=ploeg_Naam1
        self.logo_Img1=logo_Img1
        self.ploeg_Naam2=ploeg_Naam2
        self.logo_Img2=logo_Img2
        self.stadion_Naam=stadion_Naam
        self.score_ploeg_1=score_ploeg_1
        self.score_ploeg_2=score_ploeg_2
## zet hier alles van wat er in de onderste query wordt gevraagd
    def __repr__(self):
        return f'wedstijd (wedstrijd_ID={self.wedstrijd_ID},begin_Uur={self.begin_Uur}, eind_Uur={self.eind_Uur}, ploeg_Naam1={self.ploeg_Naam1}, logo_Img1={self.logo_Img1}, ploeg_Naam2={self.ploeg_Naam2}, logo_Img2={self.logo_Img2}, stadion_Naam={self.stadion_Naam},score_ploeg_1={self.score_ploeg_1},score_ploeg_2={self.score_ploeg_2})'
    
    def start ():
        pass
    
    def einde():
        pass
    
    def aflassen():
        pass
    
    def lijstWedstrijden (the_db):
        sqltxt = "Select wedstrijd_ID, begin_Uur, eind_Uur, a1.ploeg_Naam, a1.logo_Img, a2.ploeg_Naam,a2.logo_Img,  stadion.stadion_Img FROM wedstrijd inner join ploeg as a1  on wedstrijd.thuis = a1.ploeg_ID inner join ploeg as a2 on wedstrijd.bezoekers = a2.ploeg_ID inner join stadion on wedstrijd.stadion_ID = stadion.stadion_ID where  begin_Uur <= NOW() order by begin_Uur ASC;" 
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()    
        return [Wedstrijd(*row) for row in result]
        

    def eerstWedstrijd (the_db):
        sqltxt = "Select wedstrijd_ID, begin_Uur, eind_Uur, a1.ploeg_Naam, a1.logo_Img, a2.ploeg_Naam,a2.logo_Img,  stadion.stadion_Naam FROM wedstrijd inner join ploeg as a1  on wedstrijd.thuis = a1.ploeg_ID inner join ploeg as a2 on wedstrijd.bezoekers = a2.ploeg_ID inner join stadion on wedstrijd.stadion_ID = stadion.stadion_ID where  begin_Uur <= NOW() order by begin_Uur ASC limit 1;" 
        mycursor = the_db.cursor()
        mycursor = the_db.cursor()
        result = mycursor.fetchone()
        mycursor.close()
        return [Wedstrijd(*row) for row in result]
    
    def gespeeld (the_db):
        sqltxt = "Select * FROM wedstrijd inner join ploeg as a1  on wedstrijd.thuis = a1.ploeg_ID inner join ploeg as a2 on wedstrijd.bezoekers = a2.ploeg_ID inner join stadion on wedstrijd.stadion_ID = stadion.stadion_ID where  begin_Uur < NOW() order by begin_Uur ;"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchone()
        mycursor.close()
        return [Wedstrijd(*row) for row in result]
    