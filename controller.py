#controller or bussiness logic
from DBconnection import Sql
from model import users
class account:
    __connection=None
    
    def __init__(self):
        self.__connection=Sql.Connect()
    
    def Login(self,users):
        if self.__isvalidLogin(users):
            if self.__isAuthentic(users):
                self.__Authorize(users)
            else:
                users.setMessage('incorrect username or password!')
        else:
            users.setMessage("Please write a username and a password")
    
   ##logic
    def __isvalidLogin(self,users):
        if users.getUsername()!="" and users.getPassword !="":
            return True
        return False
    
    def __isAuthentic(self,users):
        cursor = self.__connection.cursor()
        cursor.execute(f"""SELECT userid FROM users WHERE username ='{users.getUsername()}' AND password ='{users.getPassword()}' """)
        record=cursor.fetchone()
        if record!=None:
            return True
        return False
        self.__connection.commit()
    def __Authorize(self,users):
        users.setMessage(f"{users.getUsername()},is logined....")


