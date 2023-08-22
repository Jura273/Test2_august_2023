
rom turtle import *
from random import randint
from time import *

def razmetka():   #функция рисует разметку полня
    t=Turtle()
    t.speed(0)
    for i in range (1,21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown()
        t.goto(-200+i*20, -100)
    t.hideturtle()


t1 = Turtle() #тут рождается новая черепашка из класса черепах
t1.shape("turtle")

exitonclick()

def razmetka():   #функция рисует разметку полня
    t=Turtle()
    t.speed(0)
    for i in range (1,21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown()
        t.goto(-200+i*20, -100)
    t.hideturtle()

    while t1.xcor() < x_finish and t2.xcor() < x_finish:
        t1.fd(randint(5, 15))
        t2.fd(randint(5, 15))

    11: 24
    Антон
    Красноперов


    x_finish = 200
    while t1.xcor() < x_finish and t2.xcor() < x_finish:
        t1.fd(randint(3, 6))
        t2.fd(randint(3, 6))
        sleep(0.05)

        if t1.xcor() >= x_finish:
            t1.write("I am the winner")
        else:
            t2.write("I am the winner")




class Dog():
    name = None

dog_1 = Dog()

class Dog():
    name = None

dog_1 = Dog()
dog_1.name = "Шарик"
print(dog_1.name)


class Dog():
    name = None
    poroda = None

dog_1 = Dog()
dog_1.name = "Шарик"
dog_1.poroda = "дворняга"
print(f"{dog_1.name = }")


class Dog():
    # name = None
    # poroda = None
    def __init__(self,name,poroda) -> None:
        self.name = name
        self.poroda = poroda

    def fas(self):
        print("Гав-гав")

dog_1 = Dog( "Бобик", "корги" )

print(f"{dog_1.name = }, {dog_1.poroda = }")
dog_1.fas()