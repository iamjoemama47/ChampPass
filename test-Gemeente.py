import os
import sys

path,_ = os.path.split(os.path.realpath(__file__))
path = os.path.join(path, "myvenv/Lib/site-packages")
if not path in sys.path:
    sys.path.append(path)



import classes.dbconfig as db
import mysql.connector
from classes.gebruiker import Gebruiker

from classes.gemeente import *


mydb = db.Connect()

# read
myGemeente = Gemeente.readGemeente(mydb,'Maldegem')
print (myGemeente)
#lijst
myGemeente = Gemeente.lijst_gemeentes(mydb)
print(myGemeente)
#create
myGemeente = Gemeente.createGemeente(mydb, 'Zeebrugge', 8380, 'BE')
print(myGemeente)

