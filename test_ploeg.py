import os
import sys

path,_ = os.path.split(os.path.realpath(__file__))
path = os.path.join(path, "myvenv/Lib/site-packages")
if not path in sys.path:
    sys.path.append(path)
    
import mysql.connector
from classes.dbconfig import Connect

from classes.ploeg import *
import classes.dbconfig as db

mydb = db.Connect()
myPloeg = Ploeg.readPloeg(mydb,"KAA Gent")
print(myPloeg)  