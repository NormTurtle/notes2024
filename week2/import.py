#  u can `import` to get some librarys which are missin
# in vanilla python

# Demonstating `math` library
# import math
#
# print(math.sqrt(16))   # 4
# print(math.factorial(5)) # 120
# print(math.pi) # 3.1459


# # Demonstating `random` library
# import random
# print(random.random())  # 0.123123141414
# #^> random number between 1 & 0
# print(random.randrange(5,10)) # 9
# #> Demonstating explicit rangeing
# # >^^ random ranging = randrange
# ---------------------------
# Other ways to `import`
# 1. the rush
#!! in this you basically get accces to all the thing provided by library
# import calendar
# print(calendar.calendar(2024))

# 2. load Specific
#!! this loads the that Specificly mentioned's commands
# form the library to the currnet code making it acccesible
# by the code standalone e.g dont need to use `.` to target it
# USEFULL if only using those limied library for project
# from calendar import calendar, month
# print(month(2024,2))

# 3. Load all
#!! by this all code from library is loaded to
#> curren project which makes it acccesible easily
#
# from calendar import *
# print(month(2024,2))

# 4. Load with variable
#!! store the imported library in a variable to use
#> can be used for whole library `calendar` or just a part of it `month`

from calendar import month as mon
print(mon(2021,12))
