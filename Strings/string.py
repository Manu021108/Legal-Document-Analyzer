'''
what is a string?
string: is sequence of characters

'',"",'''''''

-->Immutable 
                    Mutability 
                    /       \
                 Mutable   Immutable 
                   |          |
              can modify   cant modify  
              
#Indexing:

name = "M A N I S H"
        0 1 2 3 4 5 
   
SUBSTRING: SLICING   

#Syntax: name[start:end:step]  
                0  :end-1
name[0:3]
    
                               

'''
name = "Manish"
print(name)

#string methods 

print(name.capitalize())

#upper 

print(name.upper())

print(name.isupper()) # true or false 

print(name.find("M"))

#substring using slicing 
print(name[0:3])

#        -6-5-4-3-2-1
# name = "M A N I S H"
#         0 1 2 3 4 5 

print(name[0:5:2])

#Interviewer 

#can you please reverse your name using slicing 

print(name[::-1])

print(name[-1])

#methods 

string = "College"

print(string.isalpha())

#identifiers ---> var-name,class name, function name 

#keywords --- if = 10 

print(string.lower())

#counts the occurances 
print(string.count("l"))

print(string.endswith("ge"))

print(string.startswith("C"))

#strip-- removes the extra spaces 
text = " Manish "
      # 01234567
print(text)

print(text.strip())

#lstrip -->left side extra spaces removed 
#rstrip -->right side extra spaces removed 
text.rstrip()

print(text.index("M"))

frnds = "Manish rajesh"

#split --> split the string into tokens 
#text ---> list []
separated = frnds.split()

# ['Manish','Rajesh']

# Manish-Rajesh

#join ---> joins the text 
#list --> string

print("-".join(separated))


#center ---> spaces (width)

print(frnds.center(30))

#title ---> first letter to caspital 
print(frnds.title())

#swapcase--> converts caps to small and vise versa 
print(frnds.swapcase())

'''
summary:

variable rules and regulation 
strings --> craetion,slicing,indexing,methods 

REPL:
R: Read
E:Evaluate
P:Print
L:loop

Tomorrow: Problem solving (Maths)

Pre-graduate : 26th TCS NQT 
3 problems : 2 problems (4LPA) TCS 
applications : apply 

12LPA 

strings,arrays,time complexity --> 3.5 LPA 4 LPA easy 




'''
