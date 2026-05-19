from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.ticket import Ticket


tickets_bp = Blueprint('tickets', __name__)
mydb = db.Connect()

@tickets_bp.route('/tickets/<int:ticket_id>')
def ticketdetail(ticket_id):

    try:
        myticket=Ticket.get_by_id(mydb,ticket_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van tickets: {e}")
        myticket = []

    return render_template('ticketdetail.html',ticket = myticket)