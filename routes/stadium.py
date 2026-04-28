from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.ploeg import Stadium
import mysql.connector

stadium_bp = Blueprint('stadium', __name__)
mydb = db.Connect()

@stadium_bp.route('/stadium/<int:stadium_id>')
def stadium(stadium_id):
    try:
        mystadium=Stadium.get_by_id(mydb,stadium_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploegen: {e}")
        mystadium = []

    return render_template('stadium.html',stadium = mystadium)
