# a =3
# b= 6
# print(a+b)

# a = int(input("enter your age "))
# print("your age is :" , a)
# if(a>18):
#     print("you can drive")
# else:
#     print("you can not drive")    

# num = int(input("enter the number "))
# if(num<0):
#     print("num is negavtive")
# elif(num>0):
#     if(num<=10):
#         print("number is between 1-10") 
#     elif(num>10 and num<=20):
#         print("num is betwwen 10 -20")  
#     else:
#         print("num is greater than 20")         
# else:
#     print("num is zero")        


# timestamp = int(time.strftime('%H:%M:%S'))
# print(timestamp)
# timestamp = int(time.strftime('%H'))
# print(timestamp)
# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)

# import time
# name = input("enter your name ")
# timestamp = int(time.strftime('%H'))
# if(timestamp >0 and timestamp<12):
#     print("good morning ", name)
# elif(timestamp > 12 and timestamp <=6):
#     print("good afternoon")    
# elif(timestamp >6 and timestamp <=22):
#     print("good evening ", name)   
# else:
#     print("good night")    

# print("sanjay")

# x = int(input("enter the value of x"))
# match x:
#     case 0:
#         print("x is zero")
#     case 2:
#         print("x is two")    
#     case _:
#         print(x)    

# name = "sanjay"
# for i in name:
#     print(i, end=",")

# names = ["sanjay", "ravan", "ajay", "patel"]    
# for name in names:
#     print(name)
#     for i in name:
#         print(i)

# for i in range(5):
#     print(i)        

# for j in range(5 , 20):
#     print(j)

# for k in range(1,20,2):
#     print(k)

# i = 0
# while(i<=50):
#     i= int(input("enter the number"))
#     print(i)

# count = -5
# while(count > 0):
#     print(count)
#     count = count - 1
# else:
#     print("i am else")    

# for i in range(12):
#     if(i==10):
#         break
#     print("6 * ",i+1,"=", 6*(i+1))
# print("loop khatam")    

# for i in range(12):
#     if(i==10):
#         print('skip the itration')
#         continue
#     print("6 * ",i+1,"=", 6*(i+1))
# print("loop khatam")   

# i=0
# while True:
#     print(i)
#     i = i+1
#     if(i%100==0):
#         break
   
# def calculateMean(a,b):
#     mean = (a+b)/2
#     print(mean)

# def isGreater(a,b):
#     if(a>b):
#         print("first number is greater")
#     else:
#         print("second number is greater")     

# calculateMean(4,6) 
# isGreater(7,8)

# def isLesser(a,b):
#     pass

# def average(a=4, b=5):
#     print("the average is ", (a+b)/2)

# average(3,1 )    

# def meanNum(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum+i
#     print("mean is ", sum/len(numbers))   

# meanNum(1,2,3,4,5)        

# l = [2,3,56]
# print(l)
# print(type(l))
# print(l[0])

# l= [23,4,65,7,8,4]
# print(l)
# l.append(8)
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# print(l.index(4))
# print(l.count(4))
# m= l.copy()
# m[0]=9
# print(m)
# l.insert(1,456)
# print(l)
# m =[234,56,788]
# l.extend(m)
# print(l)

# tup = (1,6,7,43,6,"green")
# print(tup)
# print(tup[5])
# a = list(tup)
# a.append(6666)
# b = tuple(a)
# print(b)
# print(b.count(6))
# print(b.index(6))

# name = "sanjay"
# country = "india" 
# txt = f"hey my name is {name} and  i am from {country} "
# print(txt)

# def factorial(n):
#     if(n ==0 or n == 1):
#         return 1
#     else:
#       return  n * factorial(n-1)    

# print(factorial(5))        
# a = int(input("enter the number: "))
# def fib(n):
    
#     if(n == 0):
#         return 0
#     elif(n == 1 or n ==2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)      
# for n in range(a):
#     print(fib(n))

# san = {""}
# print(type(san))

# s1 = {2,5,6,8 }
# s2 = {24,5,7,3}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

# state1 = {"maharashtra", "goa", "uttar pradesh", "bihar"}
# state2 = {"punjab", "chennai", "utrakhnad","goa","bihar"}
# state3= state1.intersection(state2)
# print(state3)
# state4 = state1.symmetric_difference(state2)
# print(state4)
# c = state1.isdisjoint(state2)
# print(c)

# inf0 = {"name": "santosh", "age": 22, "eligible":"yes"}
# print(inf0)
# print(inf0["age"])
# print(inf0.get("age"))
# print(inf0.keys())
# for key in inf0.keys():
#     print(f"the value of corresponding to the ke {key} is {inf0[key]}")

# inf0.pop("age")
# print(inf0)

# for i in range(8):
#     print(i)
#     if(i == 5):
#         break
# else:
#     print("i am sanjay")    

# a = input("enter the number :")
# print(f"mutiplication table of {a} is")
# try:
#  for i in range(1, 11):
#     print(f"{int(a)}) * {i} = {int(a) * i} " )
# except:
#     print("invalid input!")    
# print("how are you")    
 
# a = input("enter the value between 5 and 15 :")
# if(a != "quit"):
#     raise ValueError("other than quit")
# a=input("enter value between 5 to 9")
# try:
#   if int(a)<5 or int(a)>9:
#       raise ValueError("wnter correct calue")
# except:
#   if a!='quit':
#       raise ValueError('string is not quit')
#   else:
#       print('quiting')

# import random
# for i in range(1,500):
#  a =random.randint(1,38)
#  b =random.randint(1,38)
#  c =random.randint(1,38)
#  d =random.randint(1,38)
#  e =random.randint(1,38)
#  f =a+b+c+d+e
#  if(f == 65):
#     print(a,b,c,d,e)
    # print(f)     

# fruits = ["mango", "banana", "watermelon", "apple"]    
# for index,fruit in enumerate(fruits):
#     print(index,fruit)
#     if (index == 1):
#         print("I love banana")

# import math

# r = math.sqrt(9)* math.pi
# print(r)
# print(dir(math))

# import main

# main.welcome()
# import os
# if(not os.path.exists("sanju")):
#  os.mkdir("sanju")
# for i in range(1,10):
#     os.mkdir(f"sanju/movie{i}")

# os.remove("sanju")

# import random

# msg = input(" enter your msg :")
# words = msg.split(" ")
# coding = True
# if(coding):
#     nwords = []
#     for word in words:
#         if(len(word) >= 3):
#            r1 = random.choice(["hsk","hdu", "khr", "zjg", "jdt","ght","zbt"])
#            r2 = random.choice(["ctg","mjt", "nyt","grr", "dtn","jta", "dgl"])
#            nmsg = r1 + msg[1:] + msg[0] + r2
#            nwords.append(nmsg)
#         else:
#            nwords.append(word[::-1])
#     print(" ".join(nwords))

# f = open('reading.txt', 'r')
# text = f.read()
# print(text)
# f.close()
# s = open('learn.txt', 'w')
# s.write('hello world!')
# s.close()

# f = open('TimeStam.py', 'r')
# text = f.read()
# print(text)
# i =0
# f = open('learn.txt', 'r')
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student is {i} in maths is {m1}")
#     print(f"marks of student is {i} in maths is{m2}")
#     print(f"marks of student is {i} in maths is{m3}")

# f = open('lucifer.txt','w')
# lines = ['kaka jii\n', 'line2\n', 'line3\n']
# f.writelines(lines)
# f.close()

# with open('lucifer.txt', 'w') as f:
    # print(type(f))
    # f.seek(10)
    # data = f.read(5)
    # print(data)
    # f.write('hello world!')
    # f.truncate(8)

# double = lambda x : x/7
# print(double(89))    
# def cube(x):
#     return x*x*x
# l = [1,2,3,45,4]
# sum =0
# for i in l:
#     sum = sum + i
# mean = sum/len(l)   
# print(mean)
# lambda x : x*x*x
# newl = list(map(lambda x : x*x*x, l))
# print(newl)

# class person:
#     name = "sanjay"
#     age = 21
#     occupation = "student"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = person()
# a.name = "malik"
# a.occupation = "deliveryboy"
# a.info()

# class person():
#     def __init__(self, n , o):
#         print("hey am a person") 
#         self.name = n
#         self.occ = o
#     def info(self):
#         print(f"{self.name} is a {self.occ}")    

# a = person("sanjay", "student")
# b = person("malik","madharchod")
# a.info()
# b.info()

# class MyClass:
#     def __init__(self,value):
#         self._value = value

#     def show(self):
#         print(f"value is {self._value}")    

#     @property
#     def ten_value(self):
#         return 10*self._value

#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10

# obj = MyClass(10)                
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()

# class employee():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showdetails(self):
#         print(f"The name of emplyoee : with id {self.id} is {self.name}")    

# class language(employee):
#    def showlanguage(self): 
#     print("the default language is python")
# e = language("sanjay chauhan", 300)        
# e.showdetails()
# e.showlanguage()

# class employee:
#     def __init__(self):
#         self.__name = "chacha"
# a = employee()
# print(a._employee__name)        

# class maths():
#     def __init__(self, num):
#         self.num = num

#     def addToNum(self,n):
#         self.num = self.num + n    
    
#     @staticmethod
#     def add(a ,b):
#         return a+b

# a = maths(5)        
# print(a.num)
# a.addToNum(6)
# print(a.num)
# print(a.add(4,7))

# class employee():
#     companyName = "google"
#     def __init__(self,name):
#         self.name = name
#         self.raise_amount = 2

#     def showDetails(self):
#         print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

# emp1 = employee("sanjay")  
# emp1.raise_amount = 6   
# emp1.companyName = "amzon"   
# emp1.showDetails()
# emp2 = employee("ajay")  
# # emp1.raise_amount = 6      
# emp2.showDetails()

# class Library():
#     def __init__(self):
#         self.No_of_books = 0 
#         self.books = []
    
#     def addBook(self, book):
#         self.books.append(book)
#         self.No_of_books = len(self.books)
    
#     def showInfo(self):
#         print(f"the no of books is {self.No_of_books} and the books are ")

#         for i in self.books:
#             print(i)    

# l1 = Library()
# l1.addBook("hindi") 
# l1.addBook("english")        
# l1.addBook("marathi") 
# l1.showInfo()

# class employee():
#     company = "apple"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
    
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany

# e1 = employee()
# e1.name = "sanjay"            
# e1.show()
# e1.changeCompany("google")
# e1.show()
# print(employee.company)

# class Employee():
#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary
    
#     @classmethod
#     def fromString(cls , string):
#         return cls(string.split("-")[0], string.split("-")[1])   

# e1 = Employee("sanjay", 12000) 
# print(e1.name)       
# print(e1.salary)

# string = "ajay-12000"
# e2 = Employee.fromString(string)
# print(e2.name)
# print(e2.salary)

# dobY = 2001
# cD = 2023
# print(cD-dobY)

# f = "sanjay"
# m = "mahendra"
# l = "chauhan"
# print(f,m,l)

# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count =0
# for item in result:
#     if(item == "heads"):
#         count += 1
# print(count)        

# for i in range(1,11):
#     if(i % 2 == 0):
#         continue
#     print(i*i)

# expense_list = [2340, 2500, 2100, 3100, 2980]
# expense_month = ["jan", "feb","march","april","may"]
# expense = int(input("Enter the expense amount :"))
# month = -1
# for i in range(len(expense_list)):
#     if(expense == expense_list[i]):
#         month = i
#         break
# if(month != -1):
#     print(f"you spent {expense} in {expense_month[month]}")    
# else:
#     print(expense)


# for i in range(1,6):
#     print(f"you run {i} km")
#     tired = input("are you tired :")
#     if tired == "yes":
#         break
# if(i == 5):
#     print("you completed thye race")
# else:
#     print("you did not finish the race")    

# for i in range(1,6):
#     s = ''
#     for j in range(i):
#         s += "*"
#     print(s)
# i = 10
# while(i < 16):
#     j =1
#     while(j <11 ):
#         print(i * j)
#         j += 1
#     i += 1

# class ParentClass():
#     def parent_method(self):
#         print("i am parent method")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("sanjay")
#         super().parent_method()
#     def child_method(self):
#         print(" i am child method")    

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()\


# from main import employee       

# e = employee("sanjay")        
# print(e)

# class shape():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y

# rec = shape(5,4)            
# print(rec.area())    
#     
# from PyPDF2 import PdfWriter

# newfile = PdfWriter()

# for pdf in ["C:\\Users\\sanja\\Downloads\\file1.pdf","C:\\Users\\sanja\\Downloads\\file2.pdf","C:\\Users\\sanja\\Downloads\\file3.pdf"]:
#     newfile.append(pdf)

# newfile.write("new-pdf.pdf")
# newfile.close()

class vector():
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"  

    def __add__(self,x):
        return vector(self.i+x.i, self.j+x.j, self.k+x.k)      

v1 = vector(3,4,5)        
print(v1)
v2 = vector(3,7,5)
print(v2)
print(v1+v2)
print(type(v1+v2))