from flask import Blueprint, render_template, session

import classes.dbconfig as db
import mysql.connector
from classes.wedstrijd import Wedstrijd

home_bp = Blueprint('home', __name__)
wedstrijden_bp = Blueprint('wedstrijden', __name__)
mydb = db.Connect()

@home_bp.route('/')
def home():
    #if 'login' not in session:  # check of sessie-variabele login bestaat
    #    return render_template('index.html')
    #if session['login'] == "":  #er is nog geen login gebeurd
    #            return render_template('login.html',the_comment="Je moet eerst inloggen")    
    #einde check login


    try:
        mywedstrijd=Wedstrijd.eerstWedstrijd(mydb)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van wedstrijden: {e}")
        mywedstrijd = []


    #hier komt de code voor de homepage
    print(mywedstrijd)
    return render_template('index.html', wedstrijd = mywedstrijd)
