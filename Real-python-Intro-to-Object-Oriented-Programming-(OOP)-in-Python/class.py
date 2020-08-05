"""
class is blue print to degine the object
- class have property and behaviour
- property also call attributes, attributes is two type instance attribute(object attribute)  and class attributes.
- class attributes is common to all object but instance attribute is changed object to object.
- attribute may be built in and custom
 class browser:
    int
    string
    Page - page class

    def load()
    def close()
- All python classes inherit from object class
- you can access and modify the class attributes and  object attributes using access modifier .
- you can also change the class attributes

"""


class Person:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        print('{} is walking and {} age is {}.'.format(self.name, self.name,self.age) )


class Child(Person):
    def talk(self):
        print("hoo hoo hooo")


amit = Person('amit', 34)
ian = Child('Ian', 3)

amit.swim()
ian.talk()
print(ian.species)
ian.species = 'mouse'
print(ian.species)
print(amit.species)






