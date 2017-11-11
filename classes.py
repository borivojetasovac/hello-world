#!/usr/bin/python3
class Person:
    title = ('Dr', 'Mr', 'Mrs', 'Ms')               # class attribute
    def __init__(self, name, surname, email, title = 'None'):       # self parameter MUST be explicitly exposed in the method signatures
        self.name = name
        self.surname = surname
        self.title = title                          # override class with instance attribute
        self.email = email
    def __str__(self):      # encapsulation is not enforced by Python, but a property is intended to be private if it begins with an underscore (by convention)
        return '%s %s %s, with email: %s' % (self.title, self.name, self.surname, self.email)

    @classmethod                                    # define class method with @classmethod decorator
    def classMethod(cls, text):                     # methods calling object(or instance) is stored in cls - by convention (instead of self)
        print('From class method: %s' % text)
    @staticmethod                                   # define static method with @staticmethod decorator
    def staticMethod(text):                         # static method doesn't have the calling object as the first parameter (no access to the class or instance)
        print('From static method: %s' % text)
    @property                                       # @property decorator makes a method behave like an attribute (there are also setter and deleter decorators)
    def fullname(self):
        return '%s %s' % (self.name, self.surname)

    def __eq__(self, other):                        # self == other ?
        return self.name == other.name and self.surname == other.surname
    def __gt__(self, other):                        # self > other ?
        if self.surname == other.surname:
            return self.name > other.name
        return self.surname > other.surname
# others comparison methods in term of first two:
    def __ne__(self, other):                        # self != other ?
        return not self == other                    # calls self.__eq__(other)
    def __le__(self, other):                        # self <= other
        return not self > other                     # calls self.__gt__(other)
    def __lt__(self, other):                        # self < other ?
        return not (self > other or self == other)
    def __ge__(self, other):                        # self >= other
        return not self < other

person = Person('Jane', 'Doe', 'jane.doe@example.com', 'Ms')
print(Person.title)                                 # access class attributes
print(person.title)
Person.classMethod('Test 123')
print(person.fullname)                              # no brackets!!
print(person)

stringAttribute = 'name'
print(getattr(person, stringAttribute, 'False'))    # returns attributes value if it exists and optional third parameter if not      second param must be string
print(person.name)                                  # don't use getattr to hard-code attribute names, only if that name is stored as a string
setattr(person, stringAttribute, 'Alice')
if hasattr(person, 'title'):
    print(True)
print(dir(person))                                  # list of all defined attributes and methods

# Inheritance:
class Student(Person):                              # parent classes in between brackets before the colon
    def __init__(self, *args, **kwargs):            # overrides parent __init__ method
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)              # pass current class and object, so super can find parents __init__ methods
    def enrol(self, course):
        self.classes.append(course)

# Mix-ins - not designed to stnad on its own, but to add extra functionallity to another class (through inheritance):
class LearnerMixin:         # mix-ins avoid 'Diamond problem': B and C (both have add method) inherit from A, and D inherits from B and C - which add will D inherit ?
    def __init__(self):
        self.classes = []
    def enrol(self, course):
        self.classes.append(course)
class TeacherMixin:
    def __init__(self):
        self.courses_taught = []
    def assign_teaching(self, course):
        self.courses_taught.append(course)
class Tutor(Person, LearnerMixin, TeacherMixin):    # Tutor can teach and learn at the same time now
    def __init__(self, *args, **kwargs):
        super(Tutor, self).__init__(*args, **kwargs)

# There are no abstract classes in Python, but this is used as a template:
class Shape2D:
    def area(self):
        raise NotImplementedError()
class Square(Shape2D):
    def __init__(self, width):
        self.width = width
    def area():
        return self.width ** 2
