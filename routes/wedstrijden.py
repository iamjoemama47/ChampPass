from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.wedstrijd import Wedstrijd


wedstrijden_bp = Blueprint('wedstrijden', __name__)
mydb = db.Connect()

@wedstrijden_bp.route('/wedstrijden/<int:wedstrijd_id>')
def wedstrijden(wedstrijd_ID):

    try:
        mywedstrijd=Wedstrijd.get_by_id(mydb,wedstrijd_ID)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van wedstrijden: {e}")
        mywedstrijd = []

    return render_template('tickets.html', wedstrijden = mywedstrijd)