'''
what is tuple?

Collection of elements 
strings-->immutable
Tuple -->immutable --> cant modify (once define)
list ---> mutable

Represented = (,,)


'''
#Creation a tuple

t = (1,2,3,4,5,2)
    # 0 1 2 3 4
print(t[0])

#Check for the muatbility 

# t[0] = 10 # tuple doesnt allows item assignment 
#type error

print(t.count(2))
#it allows duplicate 
print(t)

#task: create a tuple with three fruit names 
# and then count how many times banana comes

print(t.index(2))

#slicing 
print(t[0:4])


