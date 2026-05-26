import mysql.connector
from classes.dbconfig import Connect

class Shop:
    def __init__(self, ticket_ID=None, prijs=None, klant_ID=None, match_ID=None, aantal_tickets=None, betaald=None):
        self.ticket_ID = ticket_ID
        self.prijs = prijs
        self.klant_ID = klant_ID
        self.match_ID = match_ID
        self.aantal_tickets = aantal_tickets
        self.betaald = betaald
    
    def __repr__(self):
        return f'Shop (ticket_ID={self.ticket_ID}, prijs={self.prijs}, klant_ID={self.klant_ID}, match_ID={self.match_ID}, aantal_tickets={self.aantal_tickets}, betaald={self.betaald})'
    
    def betalen(self,the_db):
        sqltxt = "UPDATE ticket SET betaald = %s WHERE ticket_ID = %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt, (self.betaald, self.ticket_ID,))
        mycursor.close()
    

    def berekenPrijs(self):
        if self.aantal_tickets is not None and self.prijs is not None:
            totaal_prijs = self.aantal_tickets * self.prijs
            return totaal_prijs
        else:
            return None
        
    