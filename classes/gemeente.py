import mysql.connector
from classes.dbconfig import Connect


class gemeente:
    def __init__(self, gemeente_ID=None, gemeenteNaam=None, postcode=None,landCode=None):
        self.gemeente_ID = gemeente_ID
        self.gemeenteNaam = gemeenteNaam
        self.postcode = postcode
        self.landCode = landCode

    def createGemeente():
        pass

    def readGemeente():
        pass

    def updateGemeente():
        pass

    def deleteGemeente():
        pass