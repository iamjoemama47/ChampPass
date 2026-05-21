from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.wedstrijd import Wedstrijd


wedstrijden_bp = Blueprint('wedstrijden', __name__)
mydb = db.Connect()

@wedstrijden_bp.route('/wedstrijden')
def wedstrijden():

    print("wedstrijden called")
    try:
        mywedstrijd=Wedstrijd.lijstWedstrijden(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van wedstrijden: {e}")
        mywedstrijd = []

    print(wedstrijden)
    return render_template('wedstrijden.html', wedstrijden = mywedstrijd)