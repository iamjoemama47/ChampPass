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
import classes.dbconfig as db


mydb = db.Connect()




#update 
myTicket=Ticket.updateTicket(mydb,"1","40")
print(myTicket)

# delete 
myTicket=Ticket.deleteTicket(mydb,3)
print(myTicket)

#crear 
myTicket=Ticket.createTicket(mydb,"5","60","1","1")
print(myTicket)