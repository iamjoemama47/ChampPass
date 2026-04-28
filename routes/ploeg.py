from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.gebruiker import Gebruiker

gebruikers_bp = Blueprint('ploeg', __name__)
mydb = db.Connect()

@gebruikers_bp.route('/ploeg')
def ploeg():

    try:
        lijstPloeg=ploeg.lijstPloeg(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploeg: {e}")
        lijstPloeg = []

    return render_template('ploeg.html',ploeg = lijstPloeg)