# Advanced Python
import my_calc as calc
import numpy as np
from functools import reduce

# 1. Iterators
# my_list = [1, 3, 4, 5, 8, 3, 8]
# print("My list: \a", my_list)
# iter_odj = iter(my_list)

# # infinity loop
# while True:
#     try:
#         # get the next item
#         element = next(iter_odj)
#         print(f'The  Next element of the list is {element}')
#     except StopIteration:
#         # if StopIteration is raised, break from the loop
#         print("End of the List")
#         break

# 2. Creating a python module
# Imported my_calc module

# a = 30
# b = 40
#
# print("\n Addition: \a", calc.add(a, b))
# print("\n Subtraction: \a", calc.sub(a, b))
# print("\n Multiplication: \a", calc.prod(a, b))
# print("\n Division: \a", calc.div(a, b))

# number1 = int(input("\n Enter a Number x: \a"))
# number2 = int(input("\n Enter a Number y: \a"))

# print(f'\n Number x is {number1}')
# print(f'\n Number y is {number2}')

# print(f'\n Addition of X and Y is {calc.add(number1, number2)}')
# print(f'\n Subtraction of X and Y is {calc.sub(number1, number2)}')
# print(f'\n Multiplication of X and Y is {calc.prod(number1, number2)}')
# print(f'\n Division of X and Y is {calc.div(number1, number2)}')


# 3. Generator
# def function3():
#     yield print("\n Number 1 is 10")
#
#     yield print("\n Number 2 is 20")
#
#     yield print("\n Number 3 is 40")
#
#
# fun = function3()
# next(fun)

# 4. List Comprehension
# fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# new_list = []
#
# for x in fruits:
#     if "a" in x:
#         new_list.append(x)
#
# print(new_list)

# newlist = [each_fruit for each_fruit in fruits if "a" in each_fruit]
# print(newlist)
#
# h_letters = []
#
# for letter in "human":
#     h_letters.append(letter)
#
# print(h_letters)
#
# h_letters1 = [letter for letter in "human"]
# print(h_letters1)

# number_list = [x for x in range(20) if x % 2 == 0]
# print(number_list)

# obj = ["even" if i % 2 == 0 else "odd" for i in range(20)]
#
# print(obj)


# def double(x):
#     return x*2
#
#
# list1 = [double(x) for x in range(21)]
# print(list1)

# text = "life, uh, finds a way in a great indeed"
#
# unique_vowels = set(each_letter for each_letter in text if each_letter in 'aeiou')
# print(unique_vowels)


# squares = {i: i**2 for i in range(10)}
# print(squares)


# 5. Partial function
# def power(base, exponent):
#     print('{} to the power {} = {}'.format(base, exponent, base**exponent))
#     return base**exponent
#
#
# power(9, 2)

# 6. Decorators
# def f():
#     def g():
#         print("Hi, it's me 'g'")
#         print("Thanks for calling me")
#
#     print(" This is the function 'f'")
#     print("I am calling 'g' now: \n")
#
#     g()
#
#
# f()
#
#
# def temperature(t):
#     def celsius2fahrenheit(x):
#         return 9 * x / 5 + 32
#
#     result = "It's\a" + str(celsius2fahrenheit(t)) + "degrees!"
#     return result
#
#
# def factorial(n):
#     '''calculates the factorial of n,
#     n should be an integer and n <= 0'''
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# fact = factorial(5)
#
# print(fact)

# coefficient = [1, 28, 38, 47]
#
# for index, coeff in enumerate(coefficient[::-1]):
#     print(index, coeff)

# 7. Map, Filter and Reduce
# ==> Map
# item = [1, 2, 3, 4]
#
#
# def sqr(x):
#     return x ** 2
#
#
# print(list(map(sqr, item)))
#
#
# result = list(map(lambda x: x ** 2, item))
# print(result)
#
#
# def square(x):
#     return x ** 2
#
#
# def cube(x):
#     return x ** 3
#
#
# def sqroot(x):
#     return np.sqrt(x)
#
#
# functions = [sqroot, cube, sqroot]
#
# for r in range(5):
#     value = map(lambda x: x(r), functions)
#     print(list(value))

# def to_upper_case(s):
#     return str(s).upper()
#
#
# def print_iterator(it):
#     for x in it:
#         print(x, end=' ')
#
#     print("")
#
#
# print(list(map(to_upper_case, 'abc')))

# ==> Filter
# r = [-3, -4, 4, 3, 6, -7, -9, 10]
# result = list(filter(lambda x: x < 0, r))
#
# print(result)
#
# letters = ['a', 'e', 'i', 'o', 'u', 'f', 'v', 'h']
#
#
# def fun(text):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if text in vowels:
#         return True
#     else:
#         return "Not a vowel"
#
#
# filtered = filter(fun, letters)
# print(filtered)

# ==> Reduce
# numbers = [1, 2, 3, 4]
#
#
# def my_add(a, b):
#     return a + b
#
#
# result = reduce(my_add, numbers)
# print(result)
#
# result1 = reduce(lambda x, y: x*y, numbers)
# print(result1)

# 8. Project based on OOP
# class StackTOPn:
#     def __init__(self):
#         self.items = []
#
#     # For printing the stack contents
#     def __str__(self):
#         return " ".join([str(i) for i in self.items])
#
#     def isEmpty(self):
#         if not self.items:
#             return True
#         else:
#             return False
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return print(self.items[len(self.items)-1])
#
#     def size(self):
#         return print(len(self.items))
#
#     def display_all_items(self):
#         return print(self.items)
#
#
# if __name__ == "__main__":
#     stack = StackTOPn()
#     stack.isEmpty()
#     stack.push(8)
#     stack.push(3)
#     stack.push(4)
#     stack.push(5)
#     stack.push(7)
#     stack.push(1)
#     stack.display_all_items()
#     stack.size()
#     stack.pop()
#     stack.display_all_items()
print("hello world")
print("hello world")
print("hello world")
