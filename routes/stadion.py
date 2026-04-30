from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.stadion import Stadion
import mysql.connector

stadion_bp = Blueprint('stadion', __name__)
mydb = db.Connect()

@stadion_bp.route('/stadion/<int:stadion_id>')
def stadion(stadion_id):
    try:
        mystadion=Stadion.get_by_id(mydb,stadion_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploegen: {e}")
        mystadion = []

    return render_template('stadion.html',stadion = mystadion)
