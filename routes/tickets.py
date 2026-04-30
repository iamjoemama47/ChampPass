from flask import Blueprint, render_template

import classes.dbconfig as db
import mysql.connector
from classes.ticket import Ticket


ticketdetail_bp = Blueprint('ticketdetail', __name__)
mydb = db.Connect()

@ticketdetail_bp.route('/ticketdetail/<int:ticket_id>')
def ticketdetail(ticket_id):

    try:
        myticket=Ticket.get_by_id(mydb,ticket_id)
    except mysql.connector.Error as e:
        print(f"Fout bij ophalen van tickets: {e}")
        myticket = []

    return render_template('ticketdetail.html',ticket = myticket)