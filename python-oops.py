#Contents:-

#Python OBject Oriented Programming intro
#object = A bundle of related atttributes (variables) and methods (functions)
#  Ex. phone , cup, book
#  you need a class to create many objects
from Car import car
#class= (blueprint) used to design the structure and layoutof an object
class car:
    def __init__(self,model,year,color,for_sale): #its a constructor and is a dunder method(double underscore)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You are driving {self.model}")

#class variables
# class variables = Shared among all instances of a class
#                                Defined outside the constructor
#                                Allow you to share data among all objects created from that class
class Student:
   class_year = 2025#will be same for all instances
   num_students = 0
   def __init__(self, name, age): #this def is always executed at every created instances
       self.name = name#will be unquie for all instances
       self.age = age
       Student.num_students += 1
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

#inheritance
# Inheritance = Inherit attributes and methods from another class
#                        Helps with code reusability and extensibility
#                        class Child(Parent)
class Animal:#all the common attributes from child class is used here 
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is asleep")
class Dog(Animal):
    def speak(self):
        print("WOOF!")
class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")
dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

#multiple inheritance
# multiple inheritance = when a child class is derived from more than one parent class
class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()

#abstract classes
# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Requires children to use inherited abstract methods
#                 3. it has be to declared inside children class (every abstract method should be declared)
#                 4. you cant make object with it but only children
from abc import ABC, abstractmethod 
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stop the motorcycle")
class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
    def stop(self):
        print("You anchor the boat")
car = Car()
motorcycle = Motorcycle()
boat = Boat()

#super()
# super() = Function used in a child class to call methods from a parent class (superclass).
#                  Allows you to extend the functionality of the inherited methods
#for same/common parameter of childrens classes
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()
circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)
circle.describe()
square.describe()
triangle.describe()

#polymorphism
# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form
#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]
for shape in shapes:
    print(f"{shape.area()}cm²")

#duck typing
# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                            Object must have the minimum necessary attributes/methods
#                            "If it looks like a duck and quacks like a duck, it must be a duck."
class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("WOOF!")
class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Car:
    alive = True
    def speak(self):
        print("HONK!")
animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)

#aggregation
# Aggregation = Represents a relationship where one object (the whole)
#                           contains references to one or more INDEPENDENT objects (the parts)
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
library = Library("New York Public Library")
book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkein")
book3 = Book("The Colour of Magic", "Terry Pratchett")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print(library.name)
for book in library.list_books():
    print(book)

#composition
# Aggregation = A relationship where one object contains references to other INDEPENDENT objects
#               "has-a" relationship
# Composition = The composed object directly owns its components, which cannot exist independently
#               "owns-a" relationship
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
class Wheel:
    def __init__(self, size):
        self.size = size
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"
car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)
print(car1.display_car())
print(car2.display_car())

#nested classes
# Nested class = A class defined within another class
#                 class Outer:
#                    class Inner:
# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Keeps the namespace clean; reduces the possibility of naming conflicts
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def get_details(self):
            return f"{self.name} {self.position}"
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]
company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")
company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier")
company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")
for employee in company2.list_employees():
    print(employee)

#static methods
# Static methods = A method that belong to a class rather than any object from that class (instance)
#                                Usually used for general utility functions
# Instance methods - Best for operations on instances of the class (objects)
# Static methods - Best for utility functions that do not need access to class dat
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
print(Employee.is_valid_position("Rocket Scientist"))#static methods doesnt require object 

#class methods
# Class methods = Allow operations related to the class itself
#                               Take (cls) as the first parameter, which represents the class itself.
#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility functions that do not need access to class data
#  Class methods = Best for class-level data or require access to the class itself
class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    #INSTANCE METHOD has self
    def get_info(self):
        return f"{self.name} {self.gpa}"
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)
print(Student.get_count())
print(Student.get_average_gpa())

#magic methods
# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                                 They are automatically called by many of Python's built-in operations.
#                                 They allow developers to define or customize the behavior of objects
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
print(book1)  # Calls __str__
print(book1 == book3)  # Calls __eq__
print(book1 < book2)  # Calls ___lt__
print(book2 > book3)  # Calls __gt__
print(book1 + book2)  # Calls __add__
print("Lion" in book3)  # Calls __contains__
print(book3['title'])  # Calls __getitem__

#property decorator
# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#                        Benefit: Add additional logic when you read, write, or delete attributes
#                        Gives you a getter, setter, and deleter method
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
rectangle = Rectangle(3, 4)
rectangle.width = 5 #setter method
rectangle.height = 6
del rectangle.width #deleter method
del rectangle.height
print(rectangle.width) # getter method
print(rectangle.height)
