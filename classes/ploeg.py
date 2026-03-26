import mysql.connector
from classes.dbconfig import Connect


class Ploeg:
    def __init__(self, ploeg_naam=None, aantal_spelers=None, ploeg_ID=None, gemeente_ID=None, stadion_ID =None):
        self.ploeg_naam = ploeg_naam
        self.aantal_spelers = aantal_spelers
        self.ploeg_ID = ploeg_ID
        self.gemeente_ID = gemeente_ID
        self.stadion_ID = stadion_ID

    def createPloeg(self,the_db):
        sqltxt="insert into Ploeg(ploeg_ID, ploeg_naam, stadion_ID,gemeente_ID,aantal_spelers)Values(%s,%s,%s,%s,%s)"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(self.ploeg_naam,self.aantal_spelers,self.ploeg_ID,self.gemeente_ID,self.stadion_ID))
        mycursor.close()

    def readPloeg(the_db,klaid):
        sqltxt= "Select ploeg_ID,stadion_ID,ploeg_naam,aantal_spelers,gemeente_ID FROM ploeg like %s"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(klaid))
        result= mycursor.fetchone()
        mycursor.close()
        if result:
            return Ploeg(*result)
        else:
            return None
        
    
    def lijst_ploeg(the_db):
        sqltxt = "SELECT id, naam, paswoord, email, create_time FROM ploeg"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()
        return [Ploeg(*row) for row in result]

    def updatePloeg(self,the_db):
        sqltxt="UPDATE Ploeg set ploeg_ID=%s,stadion_ID=%s,ploeg_naam=%s, aantal_spelers=%s, gemeente_ID=%s WHERE ploeg_ID=%s"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(self.ploeg_naam,self.aantal_spelers,self.ploeg_ID,self.gemeente_ID,self.stadion_ID))
        mycursor.close()

    def deletePloeg(the_db,ploeg_ID):
        sqltxt="DELETE from Ploeg WHERE ploeg_ID=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(ploeg_ID,))
        mycursor.close()
    