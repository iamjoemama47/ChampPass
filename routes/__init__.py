
from flask import Blueprint

from .homePage import home_bp
from .about import about_bp
from .contact import contact_bp
from .login import login_bp
from  .changepw import changepw_bp
from .gebruikers import gebruikers_bp
from .gebruikerdetail import gebruikerdetail_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(changepw_bp)  
    app.register_blueprint(gebruikers_bp)  
    app.register_blueprint(gebruikerdetail_bp)  
    