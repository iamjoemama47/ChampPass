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


#myGespeelde = Wedstrijd.gespeeld(mydb)
#print(myGespeelde)

mynog_Spelen=Wedstrijd.nog_Spelen(mydb)
print(mynog_Spelen)