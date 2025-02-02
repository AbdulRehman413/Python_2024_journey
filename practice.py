# \n(esacpe sequence character) : for making more than one statement above and down
# To comment and uncomment use (#) and to automatically comment/uncomment 
# then use the shortcut ctrl + /
# '''
# nigga gigga
# wassup
# biuuuuuuu
# '''
# triple "single" commas to not execute the statement
# just write the statement in bewteen the commas 
# """ is also applicable  
# if want to highlight or want to write  something in inverted commas 
# use the syntax \" and keep on
# we can also put single inverted commas 
#just use the same \'
# separator syntax (sep="..") use any symbol to separate characters
# end syntax (end="...") use to add something consistently at the end of code
# FOUR TYPES OF VARIABLES 
# a can store integer (any numbers)
# b can store boolean (any true or false)
# c can store String (names or words)
# d can store none data type ?
#list1 = collections of different data types 
#mutable and non mutable means can be changed or cannot be 
#changable is list1 
#non changable is tuple1 
#if u want to create a code that can be changed later , use (list1)
#if u want a code that should not be changed , use (tuple1)
#mapped command(dict1) = to store someones information with a collection of data types 
#floor division operator : if dont want multiple values in the answer 
#module opaerator: just the percentage %
#for square root :  use double * (25*3)
#the coversion of one data type into another data type is called type casting

#  print(int(a) + int(b)) if string has integers . than use this command  


#  to count character in a string and to execute it 
#  use     (for character in "")
#  a = ("niggagigga ")
# for character in a 
# print(character)

# this will count the numbers and execute thema = ("pneumonoultramicrosilicovolcanoconiosis")


# for character in a:
#     print(character)
#     print(a[12])
#     print(a[11])
#     print(a[1])
#     print(a[3])


# if a character has for example 12 words and we want only four \n we will write like [print(character name[0:5])]


# for negative slicing , first count the characters of string and put the ratio of numbers of (-) how many u want to execute
#if we wanna guess what answer we will get , subtract the counted number with the wanted ratio
#strings are immutable= non changeable


# a = ("nigga ..... ?????? nigga")
# print(a.upper())
# print(a.lower())
# print(a.rstrip(".?"))
# print(a.replace("nigga", "rehman"))
# print(a.split(" "))
# blog = ("welcOME To Our WEBSITE")
# print(blog.capitalize())
# b = ("strings")
# print(b.center(109))
# print(a.count("nigga"))
#print(a.endswith("nigga"))
#c = ("ali is a good guy , and he likes to play cricket")
#print(c.find("cricket"))
#print(c.find("criciiii"))
#d = ("NIGGagigga7877")
#print(d.isalnum())
#d2 = ("GigganiggA")
#print(d2.isalpha())
#print(d2.islower())
#print(d2.isprintable())
#print(d2.isspace())
#d3 = ("To Kill A Mocking Bird")
#print(d3.istitle())
#print(d3.isupper())
#print(a.startswith("!"))
#print(d3.swapcase())
#print(d3.title())
#print(a.islower())

# time = int(input("Please enter the current time:"))
# region= str(input("enter the region (AM/PM only):")).upper().strip()

# if region == "AM":
#     if time in range (1,12):
#         print("Good morning sir")
#     elif time == 12:
#         print("Good noon sir ")
# elif region == "PM":
#     if time in range (12,6):
#         print*("Good afternoon sir")
#     elif time == 6:
#         print("Good evening sir ")
#     elif time in range (7,12):
#         print("Good night sir ")
#     elif time == 12 :
#         print ("good night sir")
# else:
#     print("enter the correct region and time")

#
# 
#  x = int(input("enter the value of x:"))
# match x:
#     case 1:
#         print("x is equal to 544833")
#     case 2:
#         print("x is 123333")
#     case _ if x!=90:
#         print("case is not equal to 90")
#     case _ if x!=80:
#         print("case is not equal to 80")


# colors= ["red", "white", "green", "yellow"]
# for color in colors:
#     print(color)
#     for char in color:
#         print(char)



# for k in range(1,12,2):
#     print(k)

# x = 5
# while(x>0):
#     print(x)
#     x= x -1


# for i in range(12):
#     if (i==10):
#         print("skip the iteration")
#         continue
#     print("5X",i , "=",5*i)


# for i in range(12):
#     print("5X",i+1, "=",5*(i+1))
#     if(i==9):
#         break

# for i in range(1,101,2):
#     print(i,end=" ")
#     if(i==50):
#         break
#     else:
#         print("mississippi")

# for i in(2,3,4,5,6,7,8):
#     if(i%2!=0):
#         continue
# print("mississippi")


# i = int(input("enter the number to see its multiplicartion table: "))
# for i in range(11):
#     for x in range(1,11):
#         print(x , "x", i+1, "=", x*(i+1))
#         if(i==9):
#             break



# def calculategmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isgreater(a,b):
#     if (a>b):
#         print("first number is greater")
#     else:
#         print("second number is greater")
# def islesser(a,b):
#     if (a<b):
#         print("first number is lesser")
#     else:
#         print("second number is lesser")
# def isequal(a,b):

#     pass


# a = 7
# b = 8
# isgreater(a,b)
# islesser(a,b)
# calculategmean(a,b)

# c = 8
# d = 9
# isgreater(c,d)
# islesser(c,d)
# calculategmean(c,d)


# l = [6,7,6,6,7,6,"harry"]
# print(l)
# print(type(l))

# # print(l[0])
# # print(l[3])
# # print(l[5])


# # print(l[-4])
# # print(l[len(l)-3])

# if 7 in l:
#     print("yes")
# else:
#     print("no")
# if "arry" in "harry":
#     print("yes")
# else:
#     print("NO")


# l = [1,32,554,63]
# print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(32))
# l.insert(2,7788)
# m = [100,5094,599]
# l.extend(m)
# j = l + m
# print(l)
# print(j)

# tup = (1,56,677,"green")
# print(type(tup),tup)
# print(tup[0])
# print(tup[-2])
# print(tup[3])
# if 56 in tup:
#     print("yes its present")
# else:
#     print("not present")

#     # tuples are unchangable
# print(tup[0:])


# tup= (4,4,23,32,23,6,6,6,32,2)
# res =tup.count(6)
# print(res)
# res= tup.index(6,5,9)
# print(res)

# res = len(tup)
# print(res)


# time = int(input("enter the time:"))
# region = str(input("enter the region (AM/PM ONLY):")).upper().strip()

# if region == "AM":
#     if time in range (1,12):
#         print("Good morning sir")
#     elif time == 12:
#         print("Good noon sir ")
# elif region == "PM":
#     if time in range (1,6):
#         print("Good afternoon sir")
#     elif time == 6:
#         print("Good evening sir ")
#     elif time in range (7,12):
#         print("Good night sir ")
#     elif time == 12 :
#         print ("good night sir")
# else:
#     print("enter the correct region and time")



# l = ["Question no.1: Which country has the most satellites in the world"]
# A = ["A)Russia"]
# B = ["B)China"]
# C = ["C)Japan"]
# D = ["D)America"]

# print (l)

# print(A)
# print(B)
# print(C)
# print(D)
# q = str(input("So what's your final answer:")).upper()

# if q == "A":
#     print("7 CROREEEEEEEE")
# else:
#     print("APKA JAWAABBBBBBBBBBBBB ....... GALAT HAI , AP KHALI HATH JAYEN GAY")

    

# letter = "my name is {} and i am from {}"
# country= "pakistan"
# name = "Abdul Rehman"

# print(letter.format(name, country))
# print(f"my name is {name} and i live in {country}")


# price = 49.9999
# seller = f"for only {price:.2f} dollars"
# print(seller)

# print(f"{2*49}")
# print(type(seller))



# def square(n):
#     '''take the value and returns its square'''
#     print(n**2)
# square(7)
# print(square.__doc__)

# def factorial(n):
#     if n ==0 or n ==1:
#         return 1
#     else:
#         return n * factorial(n-1)
    

# print(factorial(3))
# print(factorial(7))
# print(factorial(5))
# print(factorial(0))


# s = {2,2,4,4}
# print(s)
# print(type(s))

# s2 = {"bigga", 27, True , 67, 67}
# print(s2)

# abdul = set()
# print(type(abdul))

# for value in s2:
#     print(value)


#s1 = {1,2,3,3,4}
# s2 = {9,99,78,9}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul" , "delhi", "washington"}
# c1.intersection_update(c2)
# print(c1)


# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul" , "delhi", "washington"}
# c3 = c1.intersection(c2)
# print(c3)


# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul" , "delhi", "washington"}
# c3 = c1.symmetric_difference(c2)
# print(c3)

# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul" , "delhi", "washington"}
# c3 = c1.difference(c2)
# print(c3)

# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul" , "delhi", "washington"}
# c3 = c1.isdisjoint(c2)
# print(c3)

# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul"}
# c3 = c1.issuperset(c2)
# print(c3)

# c1 = {"tokyo", "lahore", "berlin" , "kabul"}
# c2 = {"lahore", "kabul" , "delhi", "washington"}
# print(c2.issubset(c1))


# c = {"lahore", "karachi","kashmir"}
# c.add("nigga")

# print(c)

# c = {"lahore", "karachi", "kashmir"}
# c.remove("lahore")

# print(c)

# c = {"lahore", "karachi", "kashmir"}
# item = c.pop()

# print(item)

# c = {"lahore", "karachi", "kashmir"}
# del c

# print(c)

# c = {"lahore", "karachi", "kashmir"}
# c.clear()

# print(c)


# dict  = {
#    85 : "moiz",
#     1: "sodagar",
#     48: "abdul rehman",
#     43:"abdul sarfraz"
# }

# print(48)

# print(dict[1])

# info = {"name":"abdul Rehman", "age":17, "eligible":"NO"}
# print(info)

# for key in info.keys():
#     print({key},{info[key]})


# print(info.items())



# ep = {323: 67, 23: 90, 48: 90}
# ep2 = {22: 78, 999: 65}
# ep.update(ep2)
# print(ep)

# ep.clear()
# print(ep)

# ep.pop(323)
# print(ep)

# ep.popitem()
# print(ep)

# del ep
# print(ep)

# if ep==ep2:
#     print("doesnt matter")
# else:
#     print("still doesnt matter")


# for i in range(8):
#     print(i)
#     if i == 6:
#         break
# else:
#     print("nah")

# i = 0
# while i<7:
#     print(i)
#     i = i+1
# else:
#     print("nah")

# for i in range(5):
#     print("iteration no {} in for loop".format(i+1))
# else:
#     print("else block in loop")




# multiplication table:
# a = input("enter the value: ")

# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")

# a = input("Enter the value: ")
#  try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("make sure to only use integers and try again")




# def func1():
#     try:
#         l = [1,3,4,6,7]
#         i = int(input("enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("some error occured")
#         return 0 
#     finally:
#         print("niga is executed")

# x = func1()
# print(x)


# def calculationtable():
#     x = int(input("enter the value: "))
#     try:
#         for i in range(1,11):
#             print(f"{int(x)} X {i} = {int(x)*i}")
#     except:
#         print("please enter the correct integer")
#     finally:
#         print("yeah its correct")


# x = calculationtable()
# print(x)


# a = int(input("enter any value bewteen 5 and 9: "))
# if a<5 or a>9:
#     raise ValueError("value should be bewteen 5 and 9")



# choice = int(input("Press 1 for Code and 2 for Decode: "))
# if choice == 1:
#     code  = (input("Enter the value you want to code: "))
#     coding = []
#     coding = True
#     if coding:
#         if (len(code)>=3):
#             a1 = "jjd"
#             a2 = "sas"
#             encoded = a1 + code[1:] + code[0] + a2
#             print(encoded)
#     else:
#             print("Your Code should be at least 3 letters long.")

# elif choice == 2:
#      code = input("Enter the value you want to decode: ")
#      coding = False
    
#      if (len(code)>=3):
        
#             code =  code[3:-3] 
#             decoded = code[-1] + code[:-1] 
#             print(decoded)
#      else:
#             print("enter correct value to decode")

#     a = 999
# b = 88828
# print(a)if a>b else print("=")if a==b else print(b)
    
    
    
    
    
    
    
    # a = 333
# b = 2929
# print("a") if a>b else print("b") if a<b else print("B")

# marks = [12,34,45,65,34,99]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("you've got 65 marks")
#     index +=1

# marks = [12,34,45,65,34,99]
# for index, mark in enumerate(marks, start=1):
#     print(mark)
#     if (index==5):
#         print("you've got shit marks")

# from math import sqrt , pi
# result = sqrt(16)* pi
# print(result)

# import math
# print(dir(math))

# from math import pi, sqrt
# result = sqrt(81)
# print(result)



# choice = int(input("Press 1 for Code and 2 for Decode: "))
# if choice == 1:
#     code  = (input("Enter the value you want to code: "))
#     coding = []
#     coding = True
#     if coding:
#         if (len(code)>=3):
#             a1 = "jsd"
#             a2 = "san"
#             encoded = a1 + code[1:] + code[0] + a2
#             print(encoded)
#     else:
#             print("Your Code should be at least 3 letters long.")

# elif choice == 2:
#      code = input("Enter the value you want to decode: ")
#      coding = False
    
#      if (len(code)>=3):
        
#             code =  code[3:-3] 
#             decoded = code[-1] + code[:-1] 
#             print(decoded)
#      else:
#             print("enter correct value to decode")


# import os

# for i in range(0,100):
#     os.rename(f"data/day{i+1}" , (f"data/nigga{i+1}"))
# import os
# folder = os.listdir("data")
# print(folder)


# for folders in folder:
#     print(folders)
#     print (os.listdir(f"data/{folders}"))


# # x = 4
# # print(x)

# def hello():
#     global x
#     x = 23
#     x =5 
#     print(x)
#     print(f"the local variable is {x}")
#     print("hello nigga")
    
# hello()
# print(f"the global variable is {x}")

# with open('myfile.txt', 'a') as f:
#     f.write("hey i am inside u")
    
#     f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()
# f = open('myfile.txt', 'a')
# print(f)
# f.write("niggas in paris")
# f.close()


# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student {i} in maths is: {m1}")
#     print(f"marks of student {i} in ict is: {m2}")
#     print(f"marks of student {i} in english is: {m3}")
#     print (line)


# f = open('myfile.txt2', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


# with open('myfile.txt', 'w') as f:
#     # print(type(f))
#     f.write('hello world')
#     f.truncate(7)
#     with open('myfile.txt', 'r') as f:
#         print(f.read())

# def double(x):
#     return x*2
# double = lambda x: x*2
# cube = lambda x: x*x*x
# avg = lambda x,y: (x+y)/2 
# print(avg(60, 32))
# print(double(5))
# print(cube(69))


# cube = lambda x: x*x*x
# l = [3,34,54,1,2,8,5]
# newl = list(map(cube, l))
# print(newl)

# ff = lambda x: x>4
# l = [3,34,54,1,2,8,5]
# nl = list(filter(ff,l))
# print(nl)

# from functools import reduce

# n = [1,2,3,4,5]
# sum = lambda x,y: x+y
# r = reduce(sum,n)
# print(r)


# a = [1,2,43]
# b = [1,2,43]
# print(a==b) #compares exact location of object
# print(a is b)# compares the value of object