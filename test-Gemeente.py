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

myGemeente = Gemeente.readGemeente(mydb,'Maldegem')
print (myGemeente)

myGemeente = Gemeente.lijst_gemeentes(mydb)
print(myGemeente)

myGemeente = Gemeente.createGemeente(mydb, 'Nieuwpoort', '8400', 'BEL')
print(myGemeente)

