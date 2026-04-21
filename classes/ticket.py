class Ticket():
    def __init__(self,ticket_ID=None,prijs=None,klant_ID=None,match_ID=None, aantal_tickets =None):
        self.ticket_ID=ticket_ID
        self.prijs = prijs
        self.klant_ID = klant_ID
        self.match_ID = match_ID
        self.aantal_tickets=aantal_tickets
    def __repr__(self):
        return f'ticket(ticket_ID={self.ticket_ID},prijs={self.prijs}, klant_ID={self.klant_ID}, match_ID={self.match_ID}, aantal_tickets={self.aantal_tickets})'
    
    def kopen ():
        pass
    def betalen():
        pass
    
    def createTicket(the_db, ticket_ID, prijs, klant_ID, match_ID):
        sqltxt = "INSERT INTO ticket (ticket_ID, prijs, klant_ID, match_ID) VALUES (%s, %s, %s, %s)"
        mycursor = the_db.cursor() 
        mycursor.execute(sqltxt, (ticket_ID, prijs, klant_ID, match_ID,))
        mycursor.close()


    def updateTicket(the_db,ticket_ID,prijs):
        sqltxt="UPDATE ticket set prijs=%s WHERE ticket_ID=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(ticket_ID,prijs,))
        mycursor.close()

    def deleteTicket(the_db,ticket_ID):
        sqltxt="DELETE from ticket WHERE ticket_ID=%s"
        mycursor=the_db.cursor()
        mycursor.execute(sqltxt,(ticket_ID,))
        mycursor.close()