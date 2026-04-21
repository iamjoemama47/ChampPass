class Ticket():
    def __init__(self,ticket_ID=None,prijs=None,klant_ID=None,match_ID=None, aantal_ticket =None):
        self.ticket_ID=ticket_ID
        self.prijs = prijs
        self.klant_ID = klant_ID
        self.match_ID = match_ID
        self.aantal_ticket=aantal_ticket
    def __repr__(self):
        return f'ticket(ticket_ID={self.ticket_ID},prijs={self.prijs}, klant_ID={self.klant_ID}, match_ID={self.match_ID}, aantal_ticket={self.aantal_ticket})'
    
    def kopen ():
        pass
    def betalen():
        pass
    
    def createTicket(self,the_db):
        sqltxt="insert into ticket(ticket_ID, prijs, klant_ID,match_ID)Values(%s,%s,%s,%s)"
        mycursor=the_db.cursour()
        mycursor.execute(sqltxt,(self.ticket_ID,self.prijs,self.klant_ID,self.match_ID))
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