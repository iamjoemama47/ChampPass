import mysql.connector
from classes.dbconfig import Connect


class ploeg:
    def __init__(self, ploeg_naam=None, aantal_spelers=None, ploeg_ID=None, gemeente_ID=None, stadion_ID =None):
        self.ploeg_naam = ploeg_naam
        self.aantal_spelers = aantal_spelers
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