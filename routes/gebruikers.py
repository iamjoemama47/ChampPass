from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.gebruiker import Gebruiker

gebruikers_bp = Blueprint('gebruikers', __name__)
mydb = db.Connect()

@gebruikers_bp.route('/gebruikers')
def gebruikers():

    try:
        lijst_gebruikers=Gebruiker.lijst_gebruikers(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van gebruikers: {e}")
        lijst_gebruikers = []

    return render_template('gebruikers.html',gebruikers = lijst_gebruikers)