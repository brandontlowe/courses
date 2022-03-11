from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []):  # Note we have given the list a default value of an empty array: this is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(65)
print(bob.grades)
print(rolf.grades)

# Note that changing Bob's grades, i.e. mutating the grade list for the "Bob" object, changes Rolf's grades
# too.
# This is because the default object for grades is created when the function is defined - NOT
# when it is called. Thus, since both student objects use this default value, and it is then mutated for
# the "bob" object by calling the take_exam method, it is mutated for the "rolf" object too - since the two
# arrays are the same object.

# A workaround is to make the type hinting optional, and the grades parameter to default to none. Then, use an or
# operator so that if no grades list is passed to the constructor, the grades will be initalised as a (unique)
# empty array

from typing import Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

james = Student("James")
hannah = Student("Hannah")

james.take_exam(72)
print(james.grades)
print(hannah.grades)