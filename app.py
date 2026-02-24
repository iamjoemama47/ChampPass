### peb
# om Flask te gebruiken: 
# maak virtual environment aan:
# python -m venv myvenv
# install de benodigde packages:
# pip install mysql-connector-python
# pip install flask
# pip install flask-bcrypt

### code for import classes
import os
import sys

path,_ = os.path.split(os.path.realpath(__file__))
path = os.path.join(path, "classes")
if not path in sys.path:
    sys.path.append(path)

### code for import routes & flask
from flask import Flask
from routes import register_blueprints


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key: Maricolen:' #secret key is nodig voor sessie-variabelen

register_blueprints(app)

# 
# #by default: http://localhost:5000/
# starten als:
# flask --app app run --debug