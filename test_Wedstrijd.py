import mysql.connector
from classes.dbconfig import Connect

from classes.wedstrijd import *
import classes.dbconfig as db

mydb = db.Connect()

#lijst
#myWedstrijd = Wedstrijd.lijstWedstrijden(mydb)
#print(myWedstrijd)

#myeerste = Wedstrijd.eersteWedstrijd(mydb)
#print(myeerste) 


#myGespeelde = Wedstrijd.eersteWedstrijd(mydb)
#print(myGespeelde)

nogSpelen = Wedstrijd.nog_Spelen(mydb)
print (nogSpelen)