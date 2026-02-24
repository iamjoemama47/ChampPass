

from flask import Blueprint, render_template,request, session
#from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
import classes.dbconfig as db
from classes.gebruiker import *
import mysql.connector



#Flask inits
changepw_bp = Blueprint('changepw', __name__)
#bcrypt = Bcrypt()

#db inits
mydb = db.Connect()

@changepw_bp.route('/changepw',methods=['POST','GET'])
def changepw():
    #check login
    if 'login' not in session:  # check of sessie-variabele login bestaat
        return render_template('login.html')    
    if session['login'] == "":  #er is nog geen login gebeurd
                return render_template('login.html',the_comment="Je moet eerst inloggen.")    
    #einde check login

    if request.method == "POST":
        my_pw1 = request.form["pw1"]
        my_pw2 = request.form["pw2"]
        if my_pw1 != my_pw2: #paswoorden niet gelijk
            return render_template('changepw.html',the_comment="Paswoorden zijn niet gelijk.")
        else: #paswoorden zijn gelijk
            try:
                Gebruiker.change_pw(mydb,session['login'],generate_password_hash(my_pw1))
            except mysql.connector.Error as err:
                return("Something went wrong: {}".format(err))
            return render_template('home.html',the_comment="Paswoord gewijzigd.")



    else: #we zijn zo op de pagina gekomen, zonder post
        if session['login'] == "":  #er is nog geen login gebeurd
            return render_template('login.html',the_comment="Je moet eerst inloggen.")
        else:
            return render_template('changepw.html')
