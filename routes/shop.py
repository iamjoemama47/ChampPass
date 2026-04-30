from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.shop import shop


shopdetail_bp = Blueprint('shopdetail', __name__)
mydb = db.Connect()

@shopdetail_bp.route('/shopdetail/<int:shop_id>')
def shopdetail(shop_id):

    try:
        myshop=shop.get_by_id(mydb,shop_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van shop: {e}")
        lijstshop = []

    return render_template('shopdetail.html',shop = myshop)