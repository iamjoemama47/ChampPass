from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.stadion import Stadion
import mysql.connector

stadion_bp = Blueprint('stadion', __name__)
mydb = db.Connect()

@stadion_bp.route('/stadion')
def stadion():
    return render_template('stadium.html')
