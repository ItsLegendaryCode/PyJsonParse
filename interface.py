import parse
from parse import *

def app():
    name = input("Hello, what is your name ?")
    age = input("How old are you ?")
    food = input("What's your favourite food ?")
    data = [f"Your name is: {name}",f" You are {age} years old", f"Your favourite food is {food}"]
    return data

LoadJsonScheme("schemes/extras/hacker.json", app())

