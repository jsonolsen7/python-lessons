# Classes, Classmethods, Staticmethods
# ------------------------------------
# from datetime import date

# class Cat:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#     def meow(self):
#         return "{} goes 'MEOWWW'".format(self.name)

# martini = Cat("Martini", "Ragdoll", 5)

# print(martini.name)
# print(martini.meow())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)

#     @staticmethod
#     def isAdult(age):
#         return age > 18

# person1 = Person("Jason", 26)
# person2 = Person.fromBirthYear("Chris", 1994)

# def main():
    # print(person1.name)
    # print(person1.age)
    # print(person1.isAdult(person1.age))
    # print(person2.name)
    # print(person2.age)


# if __name__ == "__main__":
#     main()


# Getter and Setter Methods:
# --------------------------
# import math

# class Circle:
#     def __init__(self, radius = 0):
#         self._radius = radius

#     @property
#     def radius(self):
#         print("getter method is called")
#         return self._radius
        
#     @radius.setter
#     def radius(self, value):
#         if value.isdigit():
#             print("radius was set with the setter")
#             self._radius = value
#         else:
#             print("radius must be an integer")

#     def get_area(self):
#         return pow(int(self._radius), 2) * math.pi

# new_circle = Circle(10)

# user_r = input("Please enter radius: ")
# new_circle.radius = user_r

# def main():
#     print(new_circle.radius)
#     print("The area of the circle is:", new_circle.get_area())

# if __name__ == "__main__":
#     main()


# OOP
# ---------------------------
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def print_name(self):
#         print(f"My name is {self.first_name} {self.last_name}")

# Inheritance with super
# ----------------------------
# class Coach(Person):
#     def __init__(self, first_name, last_name, cohort):

#         super().__init__(first_name, last_name)
#         self.cohort = cohort
    
#     def welcome(self):
#         print(f"Welcome to the {self.cohort}. I am your coach {self.first_name} {self.last_name}")

# ben_person = Person("Ben", "Bruton")
# ben_coach = Coach("Benjamin", "Brutal", "ASML")

# def main():
#     print(ben_person.first_name)
#     ben_person.print_name()
#     print(ben_coach.first_name)
#     ben_coach.welcome()

# if __name__ == "__main__":
#     main()


# Polymorphism
# ---------------------------
# class Bird:
#     def __init__(self, name):
#         self.name = name
    
#     def flight(self):
#         print("Some birds can fly, some cannot.")

# class Sparrow(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def flight(self):
#         print(f"A {self.name} can fly")

# class Ostrich(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def flight(self):
#         print(f"An {self.name} cannot fly.")

# bird = Bird("bird")
# sparrow = Sparrow("sparrow")
# ostrich = Ostrich("ostrich")

# def main():
#     bird.flight()
#     sparrow.flight()
#     ostrich.flight()

# if __name__ == "__main__":
#     main()

# Magic Methods
# ----------------------------
# class Wallet:
#     def __init__(self, value, unit="USD"):
#         self.value = value
#         self.unit = unit
    
#     def __str__(self):
#         return f"{self.value} {self.unit}"

#     def __add__(self, value2):
#         return Wallet(self.value + value2.value)

# my_wallet = Wallet(5000)
# another_wallet= Wallet(100)
# third_wallet = my_wallet + another_wallet

# print(another_wallet)
# print(my_wallet.value)
# print(third_wallet)


# Challenges
# ---------------------
# 1 - Classes

# class Rectangle:
#     def __init__(self, height = 0, width = 0):
#         self._height = height
#         self._width = width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def width(self):
#         return self._width
        
#     @height.setter
#     def height(self, value):
#         if value.isdigit():
#             self._height = value
#         else:
#             print("height must be an integer")

#     @width.setter
#     def width(self, value):
#         if value.isdigit():
#             self._width = value
#         else:
#             print("width must be an integer")

#     def get_area(self):
#         return int(self.height) * int(self.width)

# def main():
#     rectangle = Rectangle()
#     user_height = input("Please enter height: ")
#     rectangle.height = user_height
#     user_width = input("Please enter width: ")
#     rectangle.width = user_width
#     print(rectangle.get_area())

# if __name__ == "__main__":
#     main()

# 2 - OOP

# class Vehicle:
#     def __init__(self, color):
#         self.color = color

#     def goes_vroom(self):
#         print(f"I'm a {self.color} vehicle and I go vroom")

# class Car(Vehicle):
#     def __init__(self, color, make, speed):
#         super().__init__(color)
#         self.make = make
#         self.speed = speed

#     def goes_vroom(self):
#         print(f"I'm a {self.color} {self.make} and I travel {self.speed} mph.")

# def main():
#     vehicle = Vehicle("green")
#     car = Car("blue", "Honda", 80)
#     vehicle.goes_vroom()
#     car.goes_vroom()

# if __name__ == "__main__":
#     main()