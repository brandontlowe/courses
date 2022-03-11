# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
    
#     @classmethod
#     def class_method(cls):
#         print(f"Called class method of {cls}")

#     @staticmethod
#     def static_method():
#         print("Called static method")

# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

# ClassTest.class_method()
# ClassTest.static_method()
# test.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    # Class methods are often used to create "factories". These are
    # methods that call the constructor and return an object instance.
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)


book = Book.hardcover("Harry Potter", 1200)
light = Book.paperback("Python 101", 700)

print(book)
print(light)
