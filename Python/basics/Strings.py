#Strings in Python
str1 = "Hello, World!"
str2 = "Vidit is awesome."

print(str1)
print("UpperCase: ",str2.upper())
print(str2)
print("LowerCase: ",str2.lower())

# Multiline string
str3= '''
Vidit is awesome
Hire him
He has good problem solving skills.
'''
print(str3)

#Length of string
lenstr3 = len(str3)
print(lenstr3)

#replace
str4 = str2.replace("awesome", "powerful")
print(str4)

#capitalize
str5 = str2.capitalize()
print(str5)

#indexing and slicing
print(str2[0]) #indexing
print(str2[0:5]) #slicing

#rstrip
print(str2.rstrip("awesome."))

#endswith method
print(str2.endswith("awesome.")) #will return boolean value True or False

#find method
print(str3.find("awesome"))

#find index method
print(str3.index("hi"))

#isprintable method
print(str3.isprintable())

#isalnum method
print(str3.isalnum())

#istitle method
title = "This is Demo Title"
print(title.istitle())