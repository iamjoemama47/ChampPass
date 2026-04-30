from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.ploeg import support
import mysql.connector

support_bp = Blueprint('support', __name__)
mydb = db.Connect()

@support_bp.route('/support')
def support():
    try:
        mysupport=support.get_by_id(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploegen: {e}")
        mysupport = []

    return render_template('support.html',support = mysupport)

