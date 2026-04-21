import mysql.connector
from classes.dbconfig import Connect

from classes.wedstrijd import *
import classes.dbconfig as db

mydb = db.Connect()

#lijst
myWedstrijd = Wedstrijd.lijstWedstrijden(mydb)
print(myWedstrijd)