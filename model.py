#model

class users:
    def __init__(self):
        pass
    
    #private members
    __username = ""
    __password = ""
    __fname = ""
    __lname  = ""
    __email = ""
    __contact = ""
    __date = ""
    __address = ""
    __userid = 0
    __message = ""

    #Settings mutators
    def setUsername(self,param):
        self.__username=param
    
    def setPassword(self,param):
        self.__password=param

    def setFname(self,param):
        self.__fname=param

    def setLname(self,param):
        self.__lname=param

    def setContact(self,param):
        self.__contact=param

    
    def setDate(self,param):
        self.__date=param


    def setAddress(self,param):
        self.__address=param

    def setUserId(self,param):
        self.__userid=param


    def setMessage(self,param):
        self.__message = param
        

    def setEmail(self,param):
        self.__email=param

#Getters accessors
    
    def getUsername(self):
        return self.__username

    def getPassword(self):
      return self.__password

    def getFname(self):
      return self.__fname

    def getLname(self):
      return self.__lname

    def getEmail(self):
      return self.__email

    def getContact(self):
      return self.__contact

    def getMessage(self):
      return self.__message

    def getAddress(self):
      return self.__address

    def getDate(self):
      return self.__date
  
    def getUserid(self):
      return self.__userid



