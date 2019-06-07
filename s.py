#no argument and no return
def hello():
    print("hello rishabh")


#call a function no argument and no return 
hello()
hello()
hello()
hello()
hello()
hello()



#with argument and no return
def helloWithArgument(name,mobile):
    print("hello %s %d"%(name,mobile))

#call a function with argument and no return    
helloWithArgument("satyam",9899)
helloWithArgument("Mohan",98989)


#with argument and with return


def sum(x,y):
    z=x+y
    return z



#call a function with argument and with return
# get input from user

a=int(input("Please enter first value"))
b=int(input("Please enter first value"))

res=sum(a,b)
res1=res+10
print(res1)



















































