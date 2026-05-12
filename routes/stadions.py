from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.stadion import Stadion
import mysql.connector

stadions_bp = Blueprint('stadions', __name__)
mydb = db.Connect()

@stadions_bp.route('/stadions')
def stadions():

    try:
        lijst_stadions=Stadion.lijst_stadions(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van stadions: {e}")
        lijst_stadions = []

    return render_template('stadions.html',stadions = lijst_stadions)
