#DB connection

import sqlite3 as m

class Sql:
    message =""
    try:
      @staticmethod
      def Connect():
        con = m.connect('python.db')
    
        if con:
            Sql.message="connected"
            print(Sql.message)
            return con
    except Exception as e:
        Sql.message=e

    
    @staticmethod
    def Close(self,con):
        con.Close()
        

