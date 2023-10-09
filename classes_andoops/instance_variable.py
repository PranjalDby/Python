class Dog:
    """
    this class prints the name and age  of dog
    and has method 
    """
    # name = "LabroDour"
    # instance_age = 0
    # constructor
    def __init__(self,name,instance_age):
        self.name = name
        self.instance_age = instance_age
    def bark(self):
        """tell user that dog bark"""
        print("Dog {} Barks ,,,,,🐶🐶🐶🐶🐶🐶".format(self.name))
    
    def age(self):
        print("Dog {} is {} yrs old ".format(self.name,self.instance_age))

    def __str__(self) -> str:
        return "Hello {} you're a dog and your age is {} yrs".format(self.name,self.instance_age)

doberman = Dog("Doberman",12)
print(doberman.bark.__doc__)

saintBrenart = Dog("Saint Brenart",30)
saintBrenart.bark()
saintBrenart.age()

# inheritance

class Fruit:
    def __init__(self,color,flavour,name) -> None:
        self.flavour = flavour
        self.color =  color
        self.name = name

class Apple(Fruit):
    # def __init__(self, color, flavour,no_of_apples) -> None:
    #     super().__init__(color, flavour)
    #     self.no_of_apples = no_of_apples
    pass

class Basket:
    def __init__(self) -> None:
        self.fruit = {}

    def add_fruit(self,fruit_insta):
        self.fruit[fruit_insta.name] = fruit_insta

    

marka_jones = Apple("Red","sour","mark_jones")
papaya = Apple("yellowish","sweet","Papaya")

basket = Basket()
basket.add_fruit(marka_jones)
basket.add_fruit(papaya)

print(basket.fruit['Papaya'].color)
