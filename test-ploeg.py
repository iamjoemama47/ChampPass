import mysql.connector
from classes.dbconfig import Connect

from classes.ploeg import *
import classes.dbconfig as db

mydb = db.Connect()

#read
myPloeg = Ploeg.readPloeg(mydb,"KAA Gent")
print(myPloeg)

#lijst
myPloeg = Ploeg.lijst_ploeg(mydb)
print(myPloeg)

