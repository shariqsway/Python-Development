# Parent Class
class Mammal:
    def walk(self):
        print("walk")


# Child Class (Inherit from parent class)
class Dog(Mammal):
    def bark(self):
        print("bark")


# Child Class (Inherit from parent class)
class Cat(Mammal):
    def meow(self):
        print("meow")
    pass


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.meow()
