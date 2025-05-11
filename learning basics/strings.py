a = ("nigga ..... ?????? nigga")
print(a.upper())
print(a.lower())
print(a.rstrip(".?"))
print(a.replace("nigga", "rehman"))
print(a.split(" "))
blog = ("welcOME To Our WEBSITE")
print(blog.capitalize())
b = ("strings")
print(b.center(109))
print(a.count("nigga"))
print(a.endswith("nigga"))
c = ("ali is a good guy , and he likes to play cricket")
print(c.find("cricket"))
print(c.find("criciiii"))
d = ("NIGGagigga7877")
print(d.isalnum())
d2 = ("GigganiggA")
print(d2.isalpha())
print(d2.islower())
print(d2.isprintable())
print(d2.isspace())
d3 = ("To Kill A Mocking Bird")
print(d3.istitle())
print(d3.isupper())
print(a.startswith("!"))
print(d3.swapcase())
print(d3.title())
print(a.islower())


 # explanation of functions of given string functions down......


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