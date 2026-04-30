from flask import Blueprint, render_template, abort
import classes.dbconfig as db
import mysql.connector
from classes.shop import shop

shopdetail_bp = Blueprint('shopdetail', __name__)

@shopdetail_bp.route('/shopdetail/<int:shop_id>')
def shopdetail(shop_id):
    myshop = None  
    
    try:

        mydb = db.Connect() 
        myshop = shop.get_by_id(mydb, shop_id)
        


    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van shop: {e}")
        return "Er is een databasefout opgetreden.", 500


    if myshop is None:
        abort(404, description="Shop niet gevonden")

    return render_template('shopdetail.html', shop=myshop)