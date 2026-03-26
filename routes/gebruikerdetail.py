from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.gebruiker import Gebruiker

gebruikerdetail_bp = Blueprint('gebruikerdetail', __name__)
mydb = db.Connect()

@gebruikerdetail_bp.route('/gebruikerdetail/<int:gebruiker_id>')
def gebruikerdetail(gebruiker_id):

    try:
        mygebruiker=Gebruiker.get_by_id(mydb,gebruiker_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van gebruikers: {e}")
        lijst_gebruikers = []

    return render_template('gebruikerdetail.html',gebruiker = mygebruiker)