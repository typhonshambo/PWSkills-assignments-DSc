'''
What is multiple inheritance? 
- when we inherit the methods of two or more classes on one class
then the phenomena is known as multiple inheritance.

Write a python code to demonstrate multiple inheritance.
'''

class class1:
    def method1(self):
        print("this is from class 1")
    
class class2:
    def method2(self):
        print("this is from class 2")

class class3(class1, class2):
    pass

class3 = class3()
class3.method1()
class3.method2() #here class3 has inherited methods from both class1 as well as class2 