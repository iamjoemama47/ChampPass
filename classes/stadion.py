import mysql.connector
from classes.dbconfig import Connect

class Stadion ():
    def __init__(self,stadion_ID=None,stadion_Naam=None,aantal_Zetels=None):
        self.stadion_ID=stadion_ID
        self.stadion_Naam=stadion_Naam
        self.aantal_Zetels=aantal_Zetels
        
    def __repr__(self):
        return f'stadion(stadion_ID={self.stadion_ID},stadion_naam={self.stadion_Naam}, aantal_Zetels={self.aantal_Zetels})'
        
    #def create (self,the_db):
      #  sqltxt= "insert into Stadion(stadion_ID, stadion_Naam, aantal_Zetels) Values(%s,%s,%s)"
     #   mycursor=the_db.cursor()
      #  mycursor.execute(sqltxt,(self.stadion_ID,self.stadion_naam, self.aantal_Zetels))
      #  mycursor.close()
    
    
    def read (the_db,stadion_ID):
        sqltxt= "Select stadion_ID ,stadion_Naam , aantal_Zetels FROM stadion WHERE stadion_Naam LIKE %s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(stadion_ID,))
        result= mycursor.fetchone()
        mycursor.close()
        if result:
            return Stadion(*result)
        else:
            return None
    
    def lijst_stadion(the_db):
        sqltxt = "Select stadion_ID,stadion_Naam,aantal_Zetels FROM stadion"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,)
        result = mycursor.fetchall()
        mycursor.close()
        return [Stadion(*row) for row in result]

        
    def update (the_db ,stadion_Naam ,aantal_Zetels ,stadion_ID):
        sqltxt="UPDATE stadion SET stadion_Naam=%s, aantal_Zetels=%s WHERE stadion_ID=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(stadion_Naam, aantal_Zetels, stadion_ID,))
        mycursor.close()


    def delete (the_db,nr):
        sqltxt="DELETE from klanten WHERE nr=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(nr,))
        mycursor.close()
    
#get foto by id
    def get_by_id(the_db,stadion_ID):
        sqltxt= "Select stadion_ID ,stadion_Naam , aantal_Zetels FROM stadion WHERE stadion_ID = %s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(stadion_ID,))
        result= mycursor.fetchone()
        mycursor.close()
        if result:
            return Stadion(*result)
        else:
            return None

        
        
    