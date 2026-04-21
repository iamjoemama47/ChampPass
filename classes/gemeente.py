import mysql.connector
from classes.dbconfig import Connect


class Gemeente:
    def __init__(self, gemeente_ID=None, gemeente_naam=None, postcode=None,land_Code=None):
        self.gemeente_ID = gemeente_ID
        self.gemeente_naam = gemeente_naam
        self.postcode = postcode
        self.land_Code = land_Code
    
    def __repr__(self):
        return f'gemeente(gemeente_ID={self.gemeente_ID},gemeente_naam={self.gemeente_naam}, post_code{self.postcode}, land_code={self.land_Code})'

    def createGemeente(the_db, gemeente_naam, postcode, land_Code):
        sqltxt = "INSERT INTO gemeente (gemeente_naam, postcode, land_Code) VALUES (%s, %s, %s)"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt, (gemeente_naam, postcode, land_Code,))
        mycursor.execute("commit")
        mycursor.close()
        return Gemeente(gemeente_naam=gemeente_naam, postcode=postcode, land_Code=land_Code)    
        


    def readGemeente(the_db, gemeente_naam):
        sqltxt =  "Select gemeente_ID, gemeente_naam, postcode, land_Code FROM gemeente where gemeente_naam like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(gemeente_naam,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Gemeente(*result)
        else:
            return None
        
    def lijst_gemeentes(the_db):
        sqltxt = "SELECT gemeente_ID, gemeente_naam, postcode, land_Code FROM gemeente"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()
        return [Gemeente(*row) for row in result]
