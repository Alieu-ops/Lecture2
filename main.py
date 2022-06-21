# #  userName = "Ceesay"
# # print(userName)
# #  Number = 15
# #  print(Number)
# #  Number2 = 5
# # result = Number + Number2
# # print(result)
# # Number = 15
# # Number2 = 5
# # result =int(Number / Number2)
# # print(result)
#
# Number = 15
# Number2 = 5
# result =int(Number * Number2)
# print(result)
# c = 100
# f = int((c*9/5)+32)
# print(f)
# question1
# x = 10
# x = 20
# x = 15
# print(x)
# question2
# x = 80
# y = 8
# z = x/y
# print(z)
# question3
# question4
# x = 25
# y = 20
# z = 3
# f = 2
# w = ((x-y)*z/f)
# print(w)
# question5
# v = 20
# x = v % 2
# print(x)
# question6
# import math
# f = 3**2
# u = math.sqrt(f)
# print(u)
# import math
# # a = 4
# # vol = a**3
# # area= 6*(a**2)
# # print(f'this is the volume: {vol}')
# # print(f'this is the area: {area}')
# # q7
# # Assignment
# import math
# a = 4
# b = 21
# c = 3
# d = (b ** 2 - 4 * a * c)
# sol1 = (-b-math.sqrt(d))/(2*a)
# sol2 = (-b+math.sqrt(d))/(2*a)
# print(sol1)
# print(sol2)
# # Use comments to show life to your work(critic)



# age = int(input('What is your age: '))
# age_remaining = 90 - age
# remaining_days = age_remaining * 365
# weeks_r = age_remaining * 52
# months_r = age_remaining * 12
# print(f'You have following {months_r} months \n {weeks_r} weeks\n  {remaining_days} days to live')
# Lecture4*** Strings*****
# name = "Mitch"
# age = 26
# full_time_employee = True
# print(name, age, full_time_employee)
#Prblem was case sensitive

# x = 20
# y = 4
# print(x - y)
# #No Error
# name=input("What is your name: ").split(" ")
# print(f'Your name is {name}')
# print(type(name))
# lecture 5
# class_mate = ("Jawo", "mhmoud", "ebrima", "badou","jainaba", "abdou")
# print(class_mate[0])
# print(class_mate.index("Jawo"))
# class_mate2 = ["Jawo", "mhmoud", "ebrima", "badou",["jainaba", "abdou"], "fatou", "jama"]
# print(class_mate2[4][0])
# print(class_mate2[0:3])
# x = class_mate2.append("sundiata")
# class_mate2.insert(1,"fatou")
# print(class_mate2)
# print(class_mate2.count("fatou"))
# class_mate2.pop(2)
# print(class_mate2)
# class_mate2.clear()
# print(class_mate2)
# print(len(class_mate2))
# l = ["jawo", "mhmoud", "ebrima", "badou","jainaba"]
# l.sort()
# print(l)
# create a program whereby 3 of names each should as to be paid and total to be discount
# randomly select one he should pay the bill
# import random
# customers = input("What are your names: ").split(", ")
# Alieu = int(input("Alieu's bill is: "))
# Fatou = int(input("Fatou's bill is: "))
# Mbye = int(input("Mbye's bill is: "))
# payment = (Alieu + Fatou + Mbye) - (Alieu + Fatou + Mbye) * .15
# x = random.choice(customers)
# print(f"{x} you are the one chosen and need to pay {payment}")
# Lecture 7: Dictionaries
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#     "month" : "Jan"
# }
# thisdict.update({"year": 2020, "Day" : "Tuesday" })
#
# # print(thisdict["brand"])
# thisdict["month"] = "May"
#
#
# print(thisdict.get("car" , "This is not in the key"))
# cartype = thisdict.pop("brand")
# # thisdict.pop("brand")
# # del thisdict["month"]
# # print(thisdict)
# # print(cartype)
# # print(thisdict.keys())
# # print(thisdict.values())
# # print(thisdict.items())
# # print(len(thisdict))
# d = list[thisdict.keys()]
# print(d)
# print(type(d))


# Tuples
# my_tuple = ("Abu", "Ali", "Jai")
# print(type(my_tuple))
# print(my_tuple[1])
# x = list(my_tuple)
# x[0] = "sundiata"
# print(x)
# (jawo, Mahmoud, Jib)  = my_tuple
# print(jawo)
# print(my_tuple.count("Ali"))
# sets#
# my_set = {2,4,6,5,}
# print(my_set)
# set2 = {10, 15, 16, 19,10, 12}
# print(set2)
# indentation
# my_name = {"Abu", "Ali", "Jai"}
# for i in my_name:
#     print(i)
# my_name.add("sundiata")
# # print(my_name)
# x = {"fatou", "csay", "alex"}
# x.update("sundiata")
# print(x)
# print(x[0])
# practice
# my_tle = ("chanel", 26)
# print("Hello", my_tle[0], " you are", my_tle[1], "years old")
# frnd = ('chanel', 'mitch', 'sara', 'cynthia', 'diane', 'steeve')
# # print(frnd[0])
# # print(frnd[5])
# print(frnd[0:2])
# k = ('Ryan', 'ahmed', 25)
# print(type(k))
# print(len(k))
# my_tuple = ("hello", [87, 40, 60], "world", (10, 25, 30))
# print(my_tuple[1][1])
#tuples are immutable
# my_tuple = (40, 3, 2, [10, 4])
# my_tuple[2] = 10
# logical statement
# name = input("What is your name: ")
# wh_going = input("Where are you going: ")
# if wh_going == "Gomindz":
#     print(f'Hello {name} welcome to {wh_going}')
#     bfast = input("Have you taken breakfast?: ")
#     if bfast == "yes":
#         print("Go  to class")
#     else:
#         print("Go to  Alieu's place")
#     # print("Have a nice python class")
# elif wh_going == "UTG":
#     print("Take the MDI road")
# else:
#     print("go homee")
# value = int(input("Enter a number:  "))
# if value %2==0:
#     print("even number")
# else:
#     print("odd number")
