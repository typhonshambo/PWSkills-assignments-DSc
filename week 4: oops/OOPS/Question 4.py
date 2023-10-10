'''
What are getter and setter in python? 
Create a class and create a getter and a setter method in this
class.
'''
class student:
    def __init__(self, name, roll):
        self.__name = name
        self.__roll = roll
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
        return "done"

student = student("Shivam", 23)
print(student.get_name())
print(student.set_name("Rahul"))
print(student.get_name())