import mysql.connector
from classes.dbconfig import Connect


class Ploeg:
    def __init__(self, ploeg_ID=None, ploeg_Naam=None, gemeente_ID=None, stadion_ID=None):
        self.ploeg_ID = ploeg_ID
        self.ploeg_Naam = ploeg_Naam
        self.gemeente_ID = gemeente_ID
        self.stadion_ID = stadion_ID

    def __repr__(self):
        return f'Ploeg (ploeg_ID={self.ploeg_ID},ploeg_Naam={self.ploeg_Naam}, gemeente_ID={self.gemeente_ID}, stadion_ID={self.stadion_ID})'
    
    #def createPloeg(the_db, ploeg_ID, ploeg_Naam, gemeente_ID, stadion_ID):
     #   sqltxt="insert into Ploeg (ploeg_ID, ploeg_Naam, gemeente_ID, stadion_ID)Values(%s,%s,%s,%s)"
      #  mycursor=the_db.cursor()
       # mycursor.execute(sqltxt,(ploeg_Naam, ploeg_ID, gemeente_ID, stadion_ID,))
        #mycursor.close()

    def readPloeg(the_db, ploeg_ID):
        sqltxt= "Select ploeg_ID, ploeg_Naam, gemeente_ID, stadion_ID FROM ploeg where ploeg_Naam like %s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(ploeg_ID,))
        result= mycursor.fetchone()
        mycursor.close()
        if result:
            return Ploeg(*result)
        else:
            return None
        
    
    def lijst_ploeg(the_db):
        sqltxt = "SELECT ploeg_ID, ploeg_Naam, stadion_ID, gemeente_ID FROM ploeg"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()
        return [Ploeg(*row) for row in result]

    #def updatePloeg(the_db):
     #   sqltxt="UPDATE Ploeg set ploeg_ID=%s,stadion_ID=%s,ploeg_Naam=%s, gemeente_ID=%s WHERE ploeg_ID=%s"
      #  mycursor=the_db.cursor()
       # mycursor.execute(sqltxt,(ploeg_Naam,ploeg_ID,self.gemeente_ID,self.stadion_ID))
        #mycursor.close()

    def deletePloeg(the_db,ploeg_ID):
        sqltxt="DELETE from Ploeg WHERE ploeg_Naam=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(ploeg_ID,))
        mycursor.close()
    