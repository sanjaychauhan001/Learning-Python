# names = "sanjay,ravan"
# print(len(names))
# print(names[0:6])
# a = "mango"
# print(a[-4:-2])
# print(a.upper())
# print(a.lower())
# print(a.replace("mango","sanjay"))

# blog = "introduction tO Python"
# print(blog.capitalize())

# str = "ajay madharchod hai jhatuuu"
# print(str.find("hai"))
# str1 = "welcome1"
# print(str1.isalpha())

# import random

# for i in range(1,1000):
#     a = random.randint(0,38)
#     b = random.randint(0,38)
#     c = random.randint(0,38)
#     d = random.randint(0,38)
    
#     e = (a+b+c+d)
#     if(e==65):
#         print(a,b,c,d)
#         print(e)
#         print("ye we have got it hurryehhhh")
       
# for 18
# 7 5 26 34        
# 22 15 15 20
#17 30 3 22
#46 4 16 6
#21 40 10 1
#19 26 9 18
#43 2 6 21

#for 5
# 5 1 9 5
#9 3 5 3
# 9 1 1 9
# 3 9 2 6
# 1 6 9 4
#7 8 1 4
#9 4 0 7
#7 0 9 4
#9 1 8 2
#9 2 6 3
#7 1 6 6
#6 1 5 8\


# def welcome():
#     print("hey dost kaise ho")
# if __name__ == "__main__":
#     welcome()   

# class employee():
#     def __init__(self, name):
#      self.name = name 

#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i+1
#         return i

#     def __str__(self):
#         return f"the name of the employee is {self.name}"  

# import geometry as g

# a = g.circle_circum(6)
# print(a)

# b = g.circle_dia(3)
# print(b)

# import numpy as np
# l = [1,2,3]
# l1 = [8,9,3]
# print(l+l1)

# a = np.array([[1,3,5],[1,6,9]])
# print(a.ndim)
# print(a[0][0])  
# print(a.itemsize)

# b = range(10)
# for i in b:
#     print(b[i])]

# print(np.arange(1,10,2))
# print(np.linspace(1,5,10))
# a = np.array([[1,3,5],[1,6,9]])
# print(a.shape)
# print(a.reshape(6,1))
# print(a.ravel())
# print(np.std(a))

# def welcome():
#     print("hey welcome to my world")

# if(__name__ == "__main__"):
#      welcome()     

# import os

# os.getcwd()

# s = open('sanjay.txt','a')
# text = s.write("hey buddy how are you ")
# s.close()

# with open('sanjay.txt', 'a') as f:
#     f.write("kya tumne chai piya")

# f = open("sanjay.txt", 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)   


# def cube(x):
#     return x*x*x

# l =[2,3,53,4]
# newl = list(map(cube, l))
# print(newl)
# l = [3,5,7,5,8]
# newl = list(filter(lambda x: x>4, l))
# print(newl)

# class person():
#     name = "sanjay"
#     age = 21
#     occupation = "student"

#     def info(self):
#         print(f"my name is {self.name} i am {self.age} and my occupation is {self.occupation}")

# a = person()
# a.name = "ajay"
# a.age = 22
# a.occupation = "berojgar"
# a.info()        

# b = person()
# b.name = "patel"
# b.age = 23
# b.occupation = "student"
# b.info()   

# a = person()
# a.name = "shikha didi"
# a.age = 13
# a.occupation = "student"
# a.info()   

# class person():
#     def __init__(self,name, age, occ):
#         self.name = name
#         self.age = age
#         self.occ = occ

#     def info(self):
#         print(f"My name is {self.name} i am {self.age} years old and i am a {self.occ}")

# a = person("sanjay",21,"student")
# a.info()

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("good morning")
#         fx(*args, **kwargs)
#         print("thank you")
#     return mfx
        

# def hello():
#     print("hello sirr")        


# def add (a,b):
#     print(a+b)    

# greet(add)(3,5)


# class myclass():
#     def __init__(self,value):
#         self.value = value

#     def show(self):
#         print(f"value is {self.value}")    

#     @property
#     def ten_value(self):
#         return 10*self.value

#     @ten_value.setter
#     def ten_value(self,new_value):
#         self.value = new_value/10    

# obj1 = myclass(6)
# obj1.ten_value = 5
# print(obj1.ten_value)
# obj1.show()        


# class Employee():
#     def __init__(self, name, id):
#         self.name = name 
#         self.id = id
    
#     def show(self):
#         print(f"My name is {self.name} and employee id is {self.id}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python")        

# e1 = Employee("rohan",411)
# e1.show()

# e2 = Programmer("ajay",555)
# e2.show()
# e2.showLanguage()

# class employee():
#     def __init__(self):
#         self.__name = "sanjay"

# o = employee()
# print(o._employee__name)


# class math():
#    def __init__(self,num):
#       self.num = num

#    def addToNum(self,n):
#       self.num = self.num + n

#    @staticmethod
#    def add(a,b):
#      return a+b  

# a = math(6)
# print(a.num)
# a.addToNum(7)
# print(a.num)


# class Employee():
#     companyname = "Google"
#     NoEmployee = 0
#     def __init__(self,name):
#         self.name = name
#         self.raise_amount = 4
#         Employee.NoEmployee += 1
    
#     def showdetails(self):
#         print(f"The name od the employee is {self.name} and raise {Employee.NoEmployee} amount is{self.raise_amount} company name is{self.companyname}")

# a = Employee("sanjay")
# a.companyname = "Apple"
# a.showdetails()

# b= Employee("abhay")
# b.raise_amount = 78
# b.showdetails()

# class employee():
#     company = "apple"

#     def show(self):
#         print(f"the company name is {self.company}")  

       
#     @classmethod
#     def changeCompany(cls, changeName):
#         cls.company = changeName

# a = employee() 
# a.show()
# print(employee.company)
# a.changeCompany("Tesla")
# a.show()           
# print(employee.company)


# class parent():
#     def parent_method(self):
#         print("this is parent method")


# class child(parent):
#     def parent_method(self):
#        print("this is child's parent method") 
#        super().parent_method()       
        
#     def child_method(self):
#         print("this is child method")
#         super().parent_method()

# a = child()
# a.parent_method()
# a.child_method()

# class Employee():
#     def __init__(self,name):
#         self.name = name

#     def __len__(self):
#         i =0
#         for c in self.name:
#             i = i+1
#         return i

#     def __str__(self):
#         return f"The name of the employee is {self.name}"    


# class shape():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y

# rec  = shape(4,7)
# print(rec.area())       

# class Animal():
#     def __init__(self, name , breed):
#         self.name = name
#         self.breed = breed

#     def make_sound(self):
#         print("Sound made by the animal")    


# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name

#     def make_sound(self):
#         print("Myauuuuuuuuuuuuuu")  

#     def eat(self):
#         print("I can eat mouse and drink milk")          

# cat = Cat("billi")
# cat.make_sound()
# cat.eat()
# import cv2

# image = cv2.imread("C:\\Users\\sanja\\Downloads\\sanjay1.jpeg")

# grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# invert = cv2.bitwise_not(grey_img)
# blur = cv2.GaussianBlur(invert, (21, 21), 0)
# invertedblur = cv2.bitwise_not(blur)
# sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
# cv2.imwrite("C:\\Users\\sanja\\Downloads\\sanjay_sketch1.png", sketch)

# c = float(input("enter the temprature in celsius: "))
# f = (c*9/5)+32
# print("the temprature in ferenhite is:",f)

# p = float(input("Enter the principal amount: "))
# r = float(input("enter the rate of intrest :"))
# n = float(input("Enter the no of years:"))
# s = (p*r*n)/100
# print(s)

# for i in range(1,50):
#     if(i%2==0):
#         print(i,end=" ")

# d = dict()
# for i in range(1,11):
#     d[i] = i*i

# print(d)
# Dict1 = {"roll": 11, "name": "sanjay","sub1": 89,"sub2":87}
# for i in Dict1:
#     print(i,Dict1[i])
# total = Dict1["sub1"]+Dict1["sub2"]
# print("total",total)

num = 5
def fact1(x):
    if(x==0 or x==1):
        return 1
    else:
        return x * fact1(x-1)    

print(fact1(5))        