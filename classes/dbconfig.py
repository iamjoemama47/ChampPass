#DAL
# klasse voor database connecties
import mysql.connector


class Connect():

    def __init__(self):
        self.mydb = mysql.connector.connect(
          
            host = "localhost",
            port = 3306,
            user = "JXPP£",
            password = "Joppe3028@ug",            
            database = "champpas"
        )
        
        
    def cursor(self):
        return self.mydb.cursor()
    
    def close(self):
        self.mydb.close()