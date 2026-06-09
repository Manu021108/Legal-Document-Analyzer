'''
what is list?

list is a collection of ordered elements 

list = [,,,,,]

list is mutable--> we can modify 

allow the duplicates ---yes 

["Tomato","Grapes","banana",]

how to create list?




'''
    #   -5 -4 -3 -2 -1
list = [10,20,30,40,50]
     #   0 1  2  3  4  
     
#Indexing and slicing as string 
print(list[0:3])   

print(list[1:-1])  #4:2

# list[start:end-1:step]



#Methods: list 

#Mutability:

fruits = ["Mango","apple","guava","Grapes"]
            # 0       1       2       3

fruits[0] = "Banana"

print(fruits)

# list is mutable ---> you can modify 


fruits.append("Black berry")

print(fruits)

#Multiple Elements at a single attempt
fruits.extend(["guava","strawberry","Pine apple"])

print(fruits)

#insert adds the element at specific index
fruits.insert(0,"Teddy")

print(fruits)

#finds the index value
print(fruits.index("Teddy"))

frnds = ["Manish","Rajesh"]
        #    0        1 

print(frnds.pop(0))

print(frnds)

#remove --> removes the element
frnds.remove("Rajesh")

print(frnds)

#Prints number of occurances in a list 
print(fruits.count("guava"))


fruits.reverse()
print(fruits)

#task: create a list of 5 best frnds 
#add two more new frnds using append
#add 3 frnds at a time 
#remove the frnds at index 4
#reverse your frnds list 

#adding 3 frends at a time
frnds.extend(["a","b","c"]) 
         #      0   1   2
print(frnds)

frnds.pop(2)

print(frnds)

#this is for reversing
frnds.reverse()

print(frnds)




  