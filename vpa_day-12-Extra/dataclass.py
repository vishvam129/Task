from dataclasses import dataclass,field

@dataclass
class Point:
    x: int  # also put a default value
    y: int  # also put a default value
    hobbies:list = field(default_factory=list)

point1 = Point(5,10)
print(point1)

@dataclass
class Person:
    name: str
    age: int

person1 = Person("abc",12)
person2 = Person("abc",12)

class Person_self:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1_ = Person_self("abc",12)
person2_ = Person_self("abc",12)

print("Dataclass ",person1 == person2)
print("Normal ",person1_ == person2_)