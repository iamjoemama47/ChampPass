


from flask import Blueprint, render_template, session

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact')
def contact():
    #check login
    if 'login' not in session:  # check of sessie-variabele login bestaat
        return render_template('login.html')    
    if session['login'] == "":  #er is nog geen login gebeurd
                return render_template('login.html',the_comment="Je moet eerst inloggen.")    
    #einde check login

    #hier komt de code voor de contactpagina
    pass

    return render_template('contact.html')