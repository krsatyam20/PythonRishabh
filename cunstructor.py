'''
Constructors can be of two types.

Parameterized/arguments  Constructor
Non-parameterized/no any arguments Constructor
__init__ 
Constructors:self calling function
when we will call class function auto call 

'''

#create class and define function
class aClass:
    # Constructor with arguments
    def __init__(self,name,id):
        self.name=name
        self.id=id
        #print(self.id)
        #print(self.name)
        
    #simple function
    def show(self):
        print("name=%s id= %d "%(self.name,self.id))


#call a class and passing arguments
obj=aClass("kumar",101)
obj2=aClass("rishave",102)
obj.show()
obj2.show()

    
#second ExAMPLE

class Student:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age

        
  
#creates the object of the class Student  
s = Student("John",101,22)  
#s = Student()  TypeError: __init__() missing 3 required positional arguments: 'name', 'id', and 'age'

print("*************befoer set print***********")
print(getattr(s,'name'))
print(getattr(s,'id'))
print(getattr(s,'age'))


print("**********After set print***********")
setattr(s,'age',23)
print(getattr(s,'age'))
setattr(s,'name','kumar')
print(getattr(s,'name'))


# Constructor - non parameterized

print("************ Non parameters ***********")


class Student:        
    def __init__(self):    
        print("This is non parametrized constructor")    

    def show(self,name):    
        print("Hello",name)    

student = Student()    
#student.show("Kuldeep")         




