#import sys
#from math import sin, cos, radians
#from math import sqrt
from matplotlib import pyplot

#for i in range(0, 390, 30):
#    print (i, sin(radians(i)), cos(radians(i)))

#def say_hello(who):
#    print("Hello ", who)

#name = input("Say your name: ")

#say_hello(name)

#def sum(a, b):
#    return a + b

#def diff(a, b):
#    return a - b

#def operation(calculate_sum):
#    if calculate_sum:
#        return sum
#    else:
#        return diff

#res = operation(False)(5, 3)

## lists
#foo = [1, 2, True, "mixing type is fine"]

#foo.append(4)
#foo.insert(0, "AAA")
#del foo[2]

#print(foo)

#foo = 3, 99, False, "Abc def"
#print(foo)

##foo[0] = 4 // is not allowed because foo is now a tuple, not a list

#def func():
#    return 1, 2

#goo = func()

#print(goo)


#my_list = [0, 1, 2, 3, 4, 5]
#print(my_list)
#print(my_list[1:2]) # [1, 2]
#print(my_list[2:])  # [2, 3, 4, 5]
#print(my_list[:2])  # [0, 1]
#print(my_list[0:4:2])   # [0, 2]
#print(my_list[-3:-1])   # [3, 4]
#print(my_list[::-1])    # [5, 4, 3, 2, 1, 0]

#my_tuple = 1, 2, 3
#a, b, c = my_tuple
#print(my_tuple)

#my_list2 = [1, 2, 3]
#a, b, c = my_list2
#print(my_list2)
#print(my_list2[1])

#fruits = ["banana", "apple", "pear"]
#for fruit in fruits:
#    print(fruit)

#fruits = "bibi", "cherish", "seed"
#for fruit in fruits:
#    print(fruit)

#for i in range(0, 10, 3):
#    print(i)

#while True:
#    if input("Say exit") == "exit":
#        break;

#def fibonacci(n):
#    a = 1
#    b = 1
#    for i in range(n):
#        if n < 2:
#            yield 1
#        else:
#            c = a + b
#            a = b
#            b = c
#            yield c

#for f in fibonacci(5):
#    print(f)

#class Vector:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def length(self):
#        return sqrt(self.x ** 2 + self.y ** 2)

#v = Vector(1, 1)
#print(v.x)
#print(v.y)
#print(v.length())
#v.y = 3
#print(v.length())

#class Document:
#    def __init__(self, author, content):
#        self.author = author
#        self.content = content
#    def length(self):
#        return len(self.content)
#    def info_summary(self):
#        return "Document written by " + self.author

#class Book(Document):
#    def __init__(self, author, content, pages):
#        super().__init__(author, content)
#        self.pages = pages
#    def info_summary(self):
#        return "Book written by {} of {} pages".format(self.author, self.pages)

#book = Book("Flaviu", ".... content ....", 50)
#print(book.length())
#print(book.info_summary())

#print(isinstance(book, Book))
#print(isinstance(book, Document))
#print(isinstance(book, object))

#class Vector:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#    def __add__(self, other):
#        return Vector(self.x + other.x, self.y + other.y)

#v1 = Vector(2, 3)
#v2 = Vector(5, 6)
#v3 = v1 + v2

#class Fibonacci:
#    def __init__(self, n):
#        self.n = n
#        self.prev = 1
#        self.prev_prev = 1
#        self.i = 0
#    def __iter__(self):
#        return self
#    def __next__(self):
#        self.i += 1
#        if self.i == self.n + 1:
#            raise StopIteration
#        if self.i <= 2:
#            return 1
#        else:
#            current = self.prev + self.prev_prev
#            self.prev_prev = self.prev
#            self.prev = current
#            return current

#for fib in Fibonacci(4):
#    print(fib)

import cv2

im = cv2.imread("E:\\SetariArpi1.png")

