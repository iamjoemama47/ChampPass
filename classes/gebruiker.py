#DAL
# CRUD gebruiker
# klasse voor inloggen

import mysql.connector
from classes.dbconfig import Connect

class Gebruiker ():

    def __init__(self, id=None, naam=None, paswoord=None, email=None,create_time=None):
        self.id = id
        self.naam = naam
        self.paswoord = paswoord
        self.email = email
        self.create_time = create_time


    def __repr__(self):
        return f'Gebruiker(id={self.id},naam={self.naam}, paswoord={self.paswoord}, email={self.email}, create_time={self.create_time})'
    

    def get_by_naam (the_db,naam):
        sqltxt = "SELECT id, naam, paswoord, email, create_time FROM gebruikers WHERE naam like %s "
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(naam,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Gebruiker(*result)
        else:
            return None



    def change_pw(the_db,naam,pw):
        sqltxt = "UPDATE gebruikers SET paswoord = %s WHERE naam = %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(pw,naam))
        the_db.mydb.commit()
        mycursor.close()


if __name__ == "__main__":
    mydb = Connect()
    try:
        my_user = Gebruiker.get_by_naam(mydb,"peter")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    print(my_user)
    mydb.close()