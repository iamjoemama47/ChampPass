import os
import sys

path,_ = os.path.split(os.path.realpath(__file__))
path = os.path.join(path, "myvenv/Lib/site-packages")
if not path in sys.path:
    sys.path.append(path)



import classes.dbconfig as db
import mysql.connector
from classes.ticket import Ticket

from classes.ticket import *


mydb = db.Connect()




#update 
myTicket=Ticket.updateTicket(mydb,"1","40","2","1")
print(myTicket)


