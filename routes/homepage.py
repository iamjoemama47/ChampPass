from flask import Blueprint, render_template, session

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    if 'login' not in session:  # check of sessie-variabele login bestaat
        return render_template('login.html')
    if session['login'] == "":  #er is nog geen login gebeurd
                return render_template('login.html',the_comment="Je moet eerst inloggen")    
    #einde check login

    #hier komt de code voor de homepage
    pass
    return render_template('home.html')