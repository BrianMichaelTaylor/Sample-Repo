import math
import os
import sys
import unittest


import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get(
    "https://digitaldefynd.com/best-data-science-certification-course-tutorial/"
)
print(r.status_code)
print(r.ok)

print(110 + 100 * 1.1 ** 5)

horse = 200 - 4
cat = 598 + 25
dog = horse + cat
print("The summation of horse and cat is dog which =", dog)
print(horse - cat)
pig = horse - cat
print(dog + horse + cat + pig)


print(r.history)

