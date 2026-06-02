import mysql.connector
from classes.dbconfig import Connect

from classes.ploeg import *
import classes.dbconfig as db

mydb = db.Connect()

#read
myPloeg = Ploeg.readPloeg(mydb, "PSG")
print(myPloeg)

#lijst
myPloeg = Ploeg.lijstPloeg(mydb)
print(myPloeg)


