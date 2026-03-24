import mysql.connector
from classes.dbconfig import Connect


class Gemeente:
    def __init__(self, gemeente_ID=None, gemeenteNaam=None, postcode=None,landCode=None):
        self.gemeente_ID = gemeente_ID
        self.gemeenteNaam = gemeenteNaam
        self.postcode = postcode
        self.landCode = landCode

    def createGemeente(self,the_db):
        sqltxt = "INSERT INTO gemeente (gemeenteNaam, postcode, landCode) VALUES (%s, %s, %s)"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt(self.gemeenteNaam, self.postcode, self.landCode))
        mycursor.close()

    def readGemeente(the_db, gemeenteNaam):
        sqltxt =  "SELECT gemeenteNaam, postcoden, landCode FROM gemeente where gemeenteNaam like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(gemeenteNaam,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            Gemeente(*result)
        else:
            return None
        
    def lijst_gemeentes(the_db):
        sqltxt = "SELECT gemeente_ID, gemeenteNaam, postcode, landCode"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt)
        result = mycursor.fetchall()
        mycursor.close()
        return [Gemeente(*row) for row in result]
