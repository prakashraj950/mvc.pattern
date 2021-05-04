#controller or bussiness logic
from DBconnection import Sql
from model import users
class account:
    __connection=None
    
    def __init__(self):
        self.__connection=Sql.Connect()

    def Save(self,users):
        if self.__isvalid(users):
            if self.__sendToDatabase(users):
                users.setMessage(f"users {users.getUsername()} was registered")
            
        else:
            users.setMessage("please fill in the field")
    def __sendToDatabase(self,users):
        try:
           cursor = self.__connection.cursor()
           query = f"INSERT into 'users' VALUES('NULL','{users.getFname()}','{users.getLname()}','{users.getUsername()}','{users.getPassword()}','{users.getEmail()}','{users.getContact()}','CURRENT_DATE','{users.getAddress()}')"
           cursor.execute(query)
           return True
        except Exception as e:
            users.getMessage(e)
            return False

    def __isvalid(self,users):
        if users.getFname()!="" and users.getLname()!= "" and users.getUsername()!="" and users.getPassword()!="" and users.getEmail()!="" and users.getContact()!="" and users.getAddress()!="":
            return True
        return False

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

