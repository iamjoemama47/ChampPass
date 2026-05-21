from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.stadion import Stadion
import mysql.connector

stadion_bp = Blueprint('stadion', __name__)
mydb = db.Connect()

@stadion_bp.route('/stadion')
def stadion():

    try:
        lijst_stadions=Stadion.lijst_stadions(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van stadion: {e}")
        lijst_stadions = []

    return render_template('stadion.html',stadions = lijst_stadions)
