import mysql.connector
from classes.dbconfig import Connect

from classes.stadion import *
import classes.dbconfig as db

mydb = db.Connect()

myStadion = Stadion.read(mydb,"Maricolen Stadion")
print(myStadion)

#myStadion = Stadion.create (mydb, "3", "Eeklo Stadion", "1000")
#print (myStadion)

myStadion = Stadion.lijst_stadion(mydb)
print(myStadion)