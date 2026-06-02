from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.stadion import Stadion
import mysql.connector

shop_bp = Blueprint('shop', __name__)
mydb = db.Connect()

@shop_bp.route('/shop')
def shop():

    return render_template('shop.html')
