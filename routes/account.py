from flask import Blueprint, render_template

import classes.dbconfig as db
from classes.ploeg import Account
import mysql.connector

account_bp = Blueprint('account', __name__)
mydb = db.Connect()

@account_bp.route('/account/<int:account_id>')
def account(account_id):
    try:
        myaccount=Account.get_by_id(mydb,account_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van ploegen: {e}")
        myaccount = []

    return render_template('account.html',account = myaccount)
