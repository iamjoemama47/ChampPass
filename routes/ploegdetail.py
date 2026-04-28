from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.ploeg import Ploeg
import mysql.connector

ploegdetail_bp = Blueprint('ploegdetail', __name__)
mydb = db.Connect()

@ploegdetail_bp.route('/ploegdetail/<int:ploeg_id>')
def ploegdetail(ploeg_id):

    try:
        myploeg=Ploeg.get_by_id(mydb,ploeg_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploegen: {e}")
        lijstPloegen = []

    return render_template('ploegdetail.html',ploeg = myploeg)