class Ticket():
    def __init__(self,ticket_id=None,prijs=None,klant_ID=None,match_ID=None, aantal_ticket =None):
        self.ticket_id=ticket_id
        self.prijs = prijs
        self.klant_ID = klant_ID
        self.match_ID = match_ID
        self.aantal_ticket=aantal_ticket
    def __repr__(self):
        return f'ticket(ticket_id={self.ticket_id},prijs={self.prijs}, klant_ID={self.klant_ID}, match_ID={self.match_ID}, aantal_ticket={self.aantal_ticket})'
    
    def kopen ():
        pass
    def betalen():
        pass