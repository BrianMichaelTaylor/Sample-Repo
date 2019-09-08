import math
import os
import sys

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

