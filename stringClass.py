str = "Hi Python !"

print(str[0])
print(type(str))
print(str)

print(str[0:3])
str = "hello"   
str1 = " world"  
print(str*3) # prints HelloHelloHello  
print(str+str1)# prints Hello world   
print(str[4]) # prints o              
print(str[2:4]); # prints ll                  
print('w' in str) # prints false as w is not present in str  
print('wo' not in str1) # prints false as wo is present in str1.   

print("The string str : %s"%(str)) # prints The string str : Hello

#================

str = "javatpoint"  
# Calling function  
str2 = str.capitalize()  
# Displaying result  
print("Old value:", str)  
print("New value:", str2)


str = "hello"  
str2 = str.islower()  
# Displaying result  
print("Old value:", str)  
print("New value:", str2)


str = "12345"  
# Calling function  
str2 = str.isnumeric()  
# Displaying result  
print(str2)  


if str.isnumeric()== True:  
    print("hello is numeric")







