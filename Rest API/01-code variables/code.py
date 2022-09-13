# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
    
#     def average(self):
#         return sum(self.grades)/len(self.grades)


# student = Student("Jose", (100, 90, 85, 100))
# student2 = Student("Narely", (100, 90, 100, 100))

# print(student.name)
# print(student.average())
# print(student2.name)
# print(student2.average())
 

# class Person:
#     def __init__(self, *args):
#         name, age = args
#         self.name = name
#         self.age = age

#     # def __str__(self): # -> str:
#     #     return f"Person {self.name}, {self.age} years old."

#     def __repr__(self) -> str:
#         return f"<Person('{self.name}', {self.age})>"

# bob = Person("Bob", 35)
# print(bob)
        
    
# class ClassTest:
#     def instance_method(self):
#         print(f"Called intance_method of {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"Called class method of {cls}")

#     @staticmethod
#     def static_method():
#         print("Called static_method")

# test = ClassTest()
# test.instance_method()
# test.class_method()
# test.static_method()

# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight
    
#     def __repr__(self):
#         return f"<Book {self.name}, {self.book_type}, weigthing {self.weight}g"

#     @classmethod
#     def hardcover(cls, name , page_weight):
#         return cls(name, cls.TYPES[0] , page_weight + 100)

#     @classmethod
#     def paperback(cls, name, page_weight):
#         return cls(name, cls.TYPES[1], page_weight + 100)


# book = Book.hardcover("Harry Potter", 1500)
# light = Book.paperback("Python 101", 600)

# print(book)
# print(light)

# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []

#     def __repr__(self) -> str:
#         print(f"<Store name:{self.name}>")

#     def add_item(self, name, price):
#         self.items.append({
#             'name': name,
#             'price': price
#         })

#     def stock_price(self):
#         total = 0
#         for item in self.items:
#             total += item['price']
#         return total

#     @classmethod
#     def franchise(cls, store):
#         # Return another store, with the same name as the argument's name, plus " - franchise"
#         return cls(store.name + " - franchise")

#     @staticmethod
#     def store_details(store):
#         return "{}, total stock price: {}".format(store.name, int(store.stock_price()))
#         # Return a string representing the argument
#         # It should be in the format 'NAME, total stock price: TOTAL'

# store = Store("Test")
# new_name = Store.franchise(store)
# store.add_item("Keyboard", 150)
# print(new_name.name,store.store_details)



