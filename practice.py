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


#