import mysql.connector
from classes.dbconfig import Connect

from classes.stadion import *
import classes.dbconfig as db

mydb = db.Connect()

myStadion = Stadion.read(mydb,"Maricolen Stadion")
print(myStadion)


