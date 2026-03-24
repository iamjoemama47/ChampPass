import mysql.connector
from classes.dbconfig import Connect

class stadion ():
    def __init__(self,stadion_ID=None,stadion_naam=None,stadion_zetels=None):
        self.stadion_ID=stadion_ID
        self.stadion_naam=stadion_naam
        self.stadion_zetels=stadion_zetels
        
    def creat (self,the_db):
        sqltxt="insert into Stadion(stadion_ID, stadion_naam, stadion_zetels)Values(%s,%s,%s)"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(self.stadion_ID,self.stadion_naam, self.stadion_zetels))
        mycursor.close()
    
    
    def read (the_db,klaid):
        sqltxt= "Select stadion_ID,stadion_naam,stadion_zetels FROM klanten stadion_ID like %s"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(klaid))
        result= mycursor.fetchone()
        mycursor.close()
        if result:
            return Stadion(*result)
        else:
            return None
    
    def lijst_stadion(the_db):
        sqltxt = "Select stadion_ID,stadion_naam,stadion_zetels FROM klanten stadion_ID"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()
        return [Stadion(*row) for row in result]
        
        
    def update (self,the_db):
        sqltxt="UPDATE Stadion set stadion_ID=%s, stadion_naam=%s, stadion_zetels=%s WHERE nr=%s"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(self.stadion_ID,self.stadion_naam, self.stadion_zetels))
        mycursor.close()

        
    def delete (the_db,nr):
        sqltxt="DELETE from klanten WHERE nr=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(nr,))
        mycursor.close()
        
        
    