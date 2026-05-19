
from flask import Blueprint

from .home import home_bp
from .about import about_bp
from .contact import contact_bp
from .login import login_bp
from .changepw import changepw_bp
from .gebruikers import gebruikers_bp
from .gebruikerdetail import gebruikerdetail_bp
<<<<<<< HEAD
from .stadion import stadion_bp
=======
from .stadions import stadions_bp
from .ploegen import ploeg_bp
from .support import support_bp
from .tickets import tickets_bp
from .account import account_bp
from .ploegdetail import ploegdetail_bp
>>>>>>> 202eb97b4bf4fe16dfd6da5c22fde353bd4d6f8c


def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(changepw_bp)  
    app.register_blueprint(gebruikers_bp)  
    app.register_blueprint(gebruikerdetail_bp)
<<<<<<< HEAD
    app.register_blueprint(stadion_bp)
=======
    app.register_blueprint(stadions_bp)
    app.register_blueprint(ploeg_bp)
    app.register_blueprint(support_bp)
<<<<<<< HEAD
    app.register_blueprint(tickets_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(ploegdetail_bp)
=======
    app.register_bleuprint(tickets_bp)
    app.register_bleuprint(account_bp)
    app.register_bleuprint(ploegdetail_bp)
>>>>>>> 202eb97b4bf4fe16dfd6da5c22fde353bd4d6f8c
>>>>>>> 928c80bc422cd312636d2ec372bef20ca3f53e94
