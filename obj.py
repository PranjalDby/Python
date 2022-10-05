from classes_object import myclass
from classes_object import Car
from classes_object import Fruit
std1 = myclass("Pranjal",12,18)
std2 = myclass("Rose",23,17)
print(std1.id)
print(std2.name)
print(std1.age)
car1 = Car("Red","Mahindra")
print("car color is = " + car1.color + " company is " + car1.company)
questionarr = [
    "What color are apples?\n (a) red/green \n (b) purple\n (c) orange\n\n",
    "What color are Bananas?\n (a) Teal \n (b) Magenta\n (c) yellow\n\n",
    "What color are stawberry's?\n (a) green \n (b) red\n (c) orange\n\n",
]
question = [
    Fruit("a",questionarr[0]),
    Fruit("c",questionarr[1]),
    Fruit("b",questionarr[2])
]
def test(quess):
    score = 0
    for i in quess:
        answer = input(i.question)
        if answer == i.answer:
            score+=1
    print("Question Right = " + str(score))
    
test(question)

