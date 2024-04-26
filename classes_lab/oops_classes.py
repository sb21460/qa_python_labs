# parent class
class Bird(object):

    # class attribute

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def intro(self):
            print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

    def speak(self):
        print("My name is {}.".format(self.name))


# owl child clas
class Owl(Bird):
    def __init__(self, name, category, age):
        self.category = category
        self.age = age

        # invoking the __init__ of the parent class
        Bird.__init__(self, name)

    def details(self):
        print("My name is {}".format(self.name))
        print("I am a : {} ".format(self.category))
        print("Age: {} years".format(self.age))
    def flight(self):
        print("Owls can rotate their heads 360 degrees and fly.")


# dodo child clas
class Dodo(Bird):
    def __init__(self, name, category, age):
        self.category = category
        self.age = age

        # invoking the __init__ of the parent class
        Bird.__init__(self, name)

    def details(self):
        print("My name is {}".format(self.name))
        print("I am a : {} ".format(self.category))
        print("Age: {} years".format(self.age))

    def flight(self):
        print("Dodo's became extinct because they couldn't fly.")


# creation of an object variable or an instance
bird1 = Owl('Angel', "Owl", 12)
bird2 = Dodo('Mark', "Dodo", 5)
bird3 = Bird(bird1)

# calling a function of the class Owl using
# its instance
bird1.speak()

# calling a function of the class Dodo using
# its instance
bird2.details()

# Python Polymorphism
bird3.flight()
bird1.flight()
bird2.flight()

# Python Encapsulation
# Creating a Base class
class BirdBase:
    def __init__(self):
        self.a = "Owls can Fly"
        self.__c = "Dodo's can't Fly"

    # Creating a derived class
class Derived(BirdBase):
    def __init__(self):

        # Calling constructor of
        # Base class
        BirdBase.__init__(self)
        print("Calling private member of Bird class: ")
        print(self.__c)

# Driver code
Owl = BirdBase()
print(Owl.a)

# Dodo = Derived()
# print(Dodo.a)

# Uncommenting print(Owl.c) will
# raise an AttributeError

# Uncommenting Dodo = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

# data abstraction

# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:

    # Hidden member of MyClass
    __hiddenVariable = 10

# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)