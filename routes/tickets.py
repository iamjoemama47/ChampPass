from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.wedstrijd import Wedstrijd


tickets_bp = Blueprint('tickets', __name__)
mydb = db.Connect()

@tickets_bp.route('/tickets/<int:wedstrijd_id>')
def tickets(wedstrijd_ID):

    try:
        mywedstrijd=Wedstrijd.get_by_id(mydb,wedstrijd_ID)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van wedstrijden: {e}")
        mywedstrijd = []

    return render_template('tickets.html', wedstrijden = mywedstrijd)