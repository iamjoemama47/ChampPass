from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.wedstrijd import Wedstrijd


tickets_bp = Blueprint('tickets', __name__)
mydb = db.Connect()

#tickets_bp.route('/tickets/<int:wedstrijd_id>')
@tickets_bp.route('/tickets')
def tickets():

 #   try:
 #       mywedstrijd=Wedstrijd.get_by_id(mydb,wedstrijd_ID)
 #   except mysql.connector.Error as e:
 #       print(f"Fout bij ophalen van wedstrijden: {e}")
 #       mywedstrijd = []
    
    print("ophalen te spelen wedstrijden")
    try:
        mynog_Spelen=Wedstrijd.nog_Spelen(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van wedstrijden: {e}")
        mynog_Spelen = []

    print(mynog_Spelen)

    return render_template('tickets.html', nog_Spelen = mynog_Spelen)