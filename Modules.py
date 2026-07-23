#Modules
# math
import math

# print(math.pi)
# print(math.sqrt(56))
# print(math.pow(5,3))
# print(math.factorial(5))
# print(math.ceil(5.1))
# print(math.floor(5.9))

import calendar as c

# print(c.calendar(2026))
# print(c.month(2026,7))
# print(c.isleap(2024))
# print(c.isleap(2026))
# print(c.leapdays(2000,2030))


import random as r

# print(r.random())
# print(r.randint(10000,100000))
# print(r.randrange(5,50,5))
# l = [45,76,"Hi",True,87.33]
# print(r.choice(l))
# print(r.choices(l,k=3))

#date-time
# import datetime as dt
#
# cur_time = dt.datetime.now()
# print(cur_time)
# print(cur_time.date())
# print(cur_time.time())
# print(cur_time.year)
# print(cur_time.month)
# print(cur_time.day)
# print(cur_time.hour)
# print(cur_time.minute)
# print(cur_time.second)
# print(cur_time.microsecond)
#
# cus_time = dt.datetime(2027,1,1,12,1,1)
# print(cus_time)
# print(cus_time.year)
# print(cus_time.month)
# print(cus_time.date())
# print(cus_time.date()-cur_time.date())

import time as t

# print(t.ctime())
# print(t.strftime("%d/%m/%Y %H:%M:%S"))

# print("Hello World")
# t.sleep(3)
# print("Hello python")
# t.sleep(2)
# print("Hello java")


# pywhatkit
import pywhatkit as pk
import pyautogui as pg

# pk.search("Vijay")
# pk.playonyt("vj siddhu vlogs")

# pk.sendwhatmsg_instantly("+91 8610277272","Hello saravanan..")
# t.sleep(5)
# pg.doubleClick()


import webbrowser as wb
# wb.open("https://livewiresalem.com/index.php")
wb.open_new_tab("https://www.geeksforgeeks.org/python/introduction-to-pywhatkit-module/")
