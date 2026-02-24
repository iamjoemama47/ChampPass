#DAL
# klasse voor database connecties
import mysql.connector


class Connect():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            #host = "sql.bbnc.be",
            #port = 33336,
            #user = "wsuser",
            #password = "WSusr+MM*9990+WSuser",
            #
            #host = "192.168.0.131",
            #port = 3306,
            #user = "wsadmin",
            #password ="wsadmin-6579",
            #
            host = "localhost",
            port = 3306,
            user = "admin",
            password = "admin",            
            database = "webshop"
        )
        
        
    def cursor(self):
        return self.mydb.cursor()
    
    def close(self):
        self.mydb.close()