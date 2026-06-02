
from flask import Blueprint

from .home import home_bp
from .about import about_bp
from .contact import contact_bp
from .login import login_bp
from .changepw import changepw_bp
from .gebruikers import gebruikers_bp
from .gebruikerdetail import gebruikerdetail_bp
from .stadion import stadion_bp
#from .stadions import stadions_bp
from .ploegen import ploeg_bp
from .support import support_bp
from .tickets import tickets_bp
from .account import account_bp
from .ploegdetail import ploegdetail_bp
from .wedstrijden import wedstrijden_bp
from .shoppen import shop_bp


def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(changepw_bp)  
    app.register_blueprint(gebruikers_bp)  
    app.register_blueprint(gebruikerdetail_bp)
    app.register_blueprint(stadion_bp)
#    app.register_blueprint(stadions_bp)
    app.register_blueprint(ploeg_bp)
    app.register_blueprint(support_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(ploegdetail_bp)
    app.register_blueprint(wedstrijden_bp)  
    app.register_blueprint(shop_bp)