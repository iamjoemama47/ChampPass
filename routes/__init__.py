
from flask import Blueprint

from .home import home_bp
from .about import about_bp
from .contact import contact_bp
from .login import login_bp
from  .changepw import changepw_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(changepw_bp)    
    