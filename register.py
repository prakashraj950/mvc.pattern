#register view

from model import users
from controller import account
u = users()
ac = account()

print("-----------------------------User Registration----------------------------")

u.setUsername(input("please choose your name: "))
u.setPassword(input("please create your Password: "))
u.setFname(input("please write your first name: "))
u.setLname(input("please write your last name: "))
u.setEmail(input("please write your Email: "))
u.setContact(input("please enter your contact no: ")))
u.setAddress(input("please write your address: "))

ac.Save(u)
print(u.getMessage())