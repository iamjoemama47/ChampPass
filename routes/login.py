# use folders: static & templates

from flask import Blueprint,Flask, render_template, request, session
### PEB- 2026/02/03
#from flask_bcrypt import Bcrypt
###PEB+
from werkzeug.security import generate_password_hash, check_password_hash


import classes.dbconfig as db
from classes.gebruiker import *

#flask inits
login_bp = Blueprint('login', __name__)

### PEB- 2026/02/03
#bcrypt = Bcrypt()


#db inits
mydb = db.Connect()

@login_bp.route('/login',methods=['POST','GET'])

def login():
    if request.method == "POST":
        my_login = request.form["login"]
        my_password = request.form["paswoord"]
        # genereer voor test
        #hashed_password = bcrypt.generate_password_hash(my_password).decode('utf-8')
        #print("te stockeren pwd:",hashed_password)

        #check of gebruiker bestaat
        try:
            my_user = Gebruiker.get_by_naam(mydb,my_login)
        except mysql.connector.Error as err:
            return("Something went wrong: {}".format(err))
        print("user:",my_user)
        if my_user: #er is een gebruiker gevonden
            #controleer of paswoord moet gewijzigd worden
            if my_user.paswoord == "": #paswoord leeg, dus eentje laten aanmaken
                session['login'] = my_login
                session['userid'] = my_user.id
                return render_template("changepw.html")
            else:
                #controleer paswoord
                if check_password_hash(my_user.paswoord,my_password):
                    session['login'] = my_login
                    session['userid'] = my_user.id
                    return render_template("home.html",the_comment="Welkom "+my_login)
                else:
                    session['login'] = ""
                    session['userid'] = ""                
                    return render_template("login.html",the_comment="Paswoord niet correct")

        else: #geen gebruiker gevonden
            session['login'] = ""
            session['userid'] = ""  
            return render_template("login.html",the_comment="Gebruiker niet gekend")

    else: #we zijn zo op de pagina gekomen, zonder post
        return render_template("login.html")
    
    #return("Something went wrong, we should never get here")