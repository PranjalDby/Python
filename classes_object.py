class myclass:
    def __init__(self,name,id,age,marks):
        self.name = name
        self.id = id
        self.age = age
        self.marks = marks
    def on_pass(self):
        if(self.marks > 3.5):
            return True
        else:
            return False

class Car:
    def __init__(self,color,company):
        self.color = color
        self.company = company

class Fruit:
    def __init__(self,answer,question):
        self.answer = answer
        self.question = question


