#view

from model import users
from controller import account
u = users()
ac = account()

print("-----------------------------welcome----------------------------")

u.setUsername(input("please write your name: "))
u.setPassword(input("please write your Password: "))

ac.Login(u)

print(u.getMessage())

