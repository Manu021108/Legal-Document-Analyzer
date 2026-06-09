'''
what is file handling?

creating files 
reading the data from files 
writing the data to files 
deleting the files 

Types of files:

1.txt -->text 
example:
Hello

2.csv -->Comma Separated values
example:
name,rollno,age,branch
Manish,08,24,datascience 


3.json --> key value pairs 
"key":Value
"RollNo":08

Binary files:
1.Images 
2.Videos 
3.PDFs 
4.Executables 
.....etc  these stores data in binary format 

File operations:
1.open --> accessing the file 
2.Read --> Read the contents 
3.Write -->Add content 
4.Append--> add at the end 
5.Close --> release the resource 

'''
#Opening the file 
# file_object = open("Filename","mode")

f = open(r"C:\Users\manis\OneDrive\Desktop\Project Phase\File Handling\main.txt","r")
data = f.read()
print(data)

'''
Files modes:
Mode  Meaning
r     read
w     write
a     append
x     create
rb    read binary 
wb    write binary 
r+    read + write 

msword + Notepad +c drive + vs code 

file will be created in your system 
you just need to use it with proper location 



'''
#read line by line 
f = open("main.txt","r")

print(f.readline())
print(f.readline())

f.close()
f = open("main.txt","r")

print(f.readline())
print(f.readline())

#Reading multiple lines 
print(f.readlines())

f.close()

#writing the files 
f = open(r"C:\Users\manis\OneDrive\Desktop\Project Phase\File Handling\main.txt","w")
f.write("Hello students")
f.close()

#existing data gets erased in w mode 

#append mode 

# adds the data to end 

f = open("main.txt","a")

f.write("\new line added")

f.close()

#using with statement (Best practice)

with open("main.txt","r") as f:
    print(f.read())
    
    
'''
cleaner
safer
no need to use close()
'''
    
#file pointers concepts 

# tell() -->returns current position  
f = open(r"C:\Users\manis\OneDrive\Desktop\Project Phase\File Handling\main.txt","r")

print(f.tell())

f.read(5)

print(f.tell())

#
