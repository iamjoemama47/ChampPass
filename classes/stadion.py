import mysql.connector
from classes.dbconfig import Connect

class Stadion ():
    def __init__(self,stadion_ID=None,stadion_naam=None,stadion_zetels=None):
        self.stadion_ID=stadion_ID
        self.stadion_naam=stadion_naam
        self.stadion_zetels=stadion_zetels
        
    def __repr__(self):
        return f'stadion(stadion_ID={self.stadion_ID},stadion_naam={self.stadion_naam}, stadion_zetels={self.stadion_zetels})'
        
    #def create (self,the_db):
      #  sqltxt= "insert into Stadion(stadion_ID, stadion_Naam, stadion_zetels) Values(%s,%s,%s)"
     #   mycursor=the_db.cursor()
      #  mycursor.execute(sqltxt,(self.stadion_ID,self.stadion_naam, self.stadion_zetels))
      #  mycursor.close()
    
    
    def read (the_db,stadion_ID):
        sqltxt= "Select stadion_ID ,stadion_Naam , aantal_zetels FROM stadion WHERE stadion_Naam LIKE %s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(stadion_ID,))
        result= mycursor.fetchone()
        mycursor.close()
        if result:
            return Stadion(*result)
        else:
            return None
    
    def lijst_stadion(the_db):
        sqltxt = "Select stadion_ID,stadion_naam,aantal_zetels FROM stadion"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,)
        result = mycursor.fetchall()
        mycursor.close()
        return [Stadion(*row) for row in result]

        
    def update (self,the_db):
        sqltxt="UPDATE Stadion set stadion_naam=%s, stadion_zetels=%s WHERE nr=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(self.stadion_ID,self.stadion_naam, self.stadion_zetels))
        mycursor.close()

        
    def delete (the_db,nr):
        sqltxt="DELETE from klanten WHERE nr=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(nr,))
        mycursor.close()
        
        
    