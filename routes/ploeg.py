from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.ploeg import Ploeg
import mysql.connector


ploeg_bp = Blueprint('ploeg', __name__)
mydb = db.Connect()

@ploeg_bp.route('/ploeg')
def ploeg():

    try:
        lijstPloeg=Ploeg.lijstPloeg(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploeg: {e}")
        lijstPloeg = []

    return render_template('ploeg.html',ploeg = lijstPloeg)