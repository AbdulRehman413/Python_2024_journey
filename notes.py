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
# just use the same \'
# separator syntax (sep="..") use any symbol to separate characters
# end syntax (end="...") use to add something consistently at the end of code
# FOUR TYPES OF VARIABLES 
# a can store integer (any numbers)
# b can store boolean (any true or false)
# c can store String (names or words)
# d can store none data type ?
# list1 = collections of different data types 
# mutable and non mutable means can be changed or cannot be 
# changable is list1 
# non changable is tuple1 
# if u want to create a code that can be changed later , use (list1)
# if u want a code that should not be changed , use (tuple1)
# mapped command(dict1) = to store someones information with a collection of data types 
# floor division operator : if dont want multiple values in the answer 
# module opaerator: just the percentage %
# for square root :  use double * (25*3)
# the coversion of one data type into another data type is called type casting

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
# if we wanna guess what answer we will get , subtract the counted number with the wanted ratio
# strings are immutable= non changeable

# print(a.upper()) to convert the string into uppercase letters
# print(a.lower()) to convert string into lowecase letters
# print(a.rstrip()) puts symbols at the beginnning or end of string 
# for example if we want to end every statement with full stop(.) , we can just put (print(a.rstrip()))
# print(a.replace("  ", "  ")) replace one string with another
# print(b.split(" ")) creates gap bewteen strings and convert it to separate components
# print(c.capitalize()) converts only first letter of string into uppercase and converts else into lowercase
# print(c.center(integers)) creates space at the beginning of strings how many length as we wants
# print(a.count()) counts how many times a sring is repeating in a statement
# print(a.endswith("symbol")) shows true or false if a string is ending with the symbol we listed in the code
# print(a.find("anything")) shows if the mentioned word is present in a string and only shows the number where mentioned string is present
# print(a.index("anything")) is same as the print(a.find("anything"))
# print(d.isalnum()) returns true if (a-z, A-Z , 0-9) are present in a string else returns false
# print(d.isalpha()) returns false (a-z, A-Z , 0-9) , its only accepts (a-z, A-Z ) and will return true on this 
# print(d.islower()) returns true if all the letters in strings are true else returns false
# print(d.isprintable()) returns true if the string has all printable characters and returns false if string has non printable character (eg. \n)
# print(d.ispace()) returns true if strings has spaces and false if string doesnt have spaces 
# print(d.istitle()) returns true if first letter of each strings is capital
# print(d.isupper()) Return True if the string is an uppercase string, False otherwise.
# print(a.startswith(".")) returns true if string starts with the mentioned symbol or letter
# print(d.swapcase()) converts uppercase into lowecase and lowercase into uppercase
# print(b.title()) converts the every first letter of string into capital
# conditional operators (<,>,<=,>=,==,!=)
# if  a statement is true it will evaluate into (if) if wromg then will use (else) to represnt it


#match case command is use to match some different cases and execute the case that is most related and acceptable

# in while loop command , the condition will repeat and repeat untill the condition and fully satisfied and it will come out of interpreter
# for loops needs a variable or string to run 
# while loop runs on some conditions , ill learn the conditions 

# break command represents leaving the loop
# continue command represents leaving the iteration


# geometric mean = ab/a+b


# def calculategmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# just a small exapmle of how to use functions(def) python, follow this method ......
# lists can be changed but tuples are unchangeable
# for lists and data entry , use square brackets for the value 

# types of list:

# l.append(  ) can be used to add integer , boolean, or string in the list
# l.sort() arrange the list into ascending order
# l.sort(reverse=True) will be arranged into descending order
# l.reverse() just reverse the origional list
# print(l.index(  )) returns the position of the mentioned int or string and represent it with number
# and if multiple int or strings are present , it will only count out the first occurence
# print(l.count(  )) returns how many times a string or int are occuring in the list
# l.insert(two integers ,(one will tell the position, second will be the value to add)), works almost same as append
# but u can choose where to add the value
# l.extend(  ) is used to add 2 lists together , the second list will be add after the first list



# instead of using formats in strings we can use f_string
# f_strings are use for data entry types , example is in the practice


# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!




# factorial means , if we put any value , its factorial method will be , it will keep multiplying with numbers 
# in descending order untill it reaches to 1
# the factorial of 0 is 1

# sets does not repeat values in list
# sets does not maintain order (ascending/descsending*)
# we use curly brackets for sets



# for union we need 2 sets , union is used to add 2 sets together
# update is used to add the value of one set into the other set
# intersection in sets will print out the common values in the existing sets 
# every string in the sets need have their own inverted commas to exist as string
# intersection update just points out the common values and remove the other non repeating values


# symmetric difference = (A union B) - (A intersection B)
# symmetric_difference will point out the uncommon values in the existing sets


# difference will point out the uncommon values from the only first set
# isdisjoint returns false if common values are present in both the sets
# issuperset returns true if the only mentioned values of set2 are present in set1
# isssubset is just the opposite of issuperset , it will show of set1 is subset of set2
# add command is just use to add values in the sunject = hence sets can be changed
# remove/discard are used to remove values from sets , just the differnce is , remove shows error if the 
# mentioned value to be removed is not present in the set and discard doesnt show error
# pop just pops out random value from the set
# del just deletes out the whole set and if u look for it to print the deleted set , it will show error
# clear command will just clear out the wanted command and will not show the error



# print(info.get[]) i dictionaries will not give error if unknown value is entered and will just show none
# print(info[]) will show error if unknown value is entered
# print(info.keys()) will point out all the keys used in the code and will not give values
# print(info.values())will give out the values from the code
# print(info.items())will give out each separate pairs
# update method in dicts updates and add values of other dict into the wanted dict
# clear command in dict just clears out the dict
# pop method pops out and removes the mentioned value from the dict
# (popitem) command pops out and removes the last value in the dict
# del command just deletes out the whole set or dict and if u try to print out the del value , youll get an error
# instead use clear/discard/remove to get no error