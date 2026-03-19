import mysql.connector
from classes.dbconfig import Connect


class ploeg:
    def __init__(self, ploegNaam=None, aantalSpelers=None, ploeg_ID=None, gemeente_ID=None, stadion_ID =None):
        self.ploegNaam = ploegNaam
        self.aantalSpelers = aantalSpelers
        self.ploeg_ID = ploeg_ID
        self.gemeente_ID = gemeente_ID
        self.stadion_ID = stadion_ID

    def createPloeg():
        pass

    def readPloeg():
        pass

    def updatePloeg():
        pass

    def deletePloeg():
        pass