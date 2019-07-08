import re


#findall() 

str = "The rain in India"
x = re.findall("ai", str)

print(x)


#search()
rishav = "The rain"
x = re.search("^The.*rain$", rishav)
# start with the and end with rain	
print(x)


#split()
splitRes=re.split("\s",str)  #\s is a spase
print(splitRes)


#sub
print("=========Before Replace ======")
print(str)

subRes=re.sub("India","World cop win by India",str)  #\s is a spase

print("========After Replace =========")
print(subRes)



subRes=re.sub("The rain in","Hello Rishave",subRes)  

print("========The Rain replac  Hello  Rishave by After Replace =========")
print(subRes)




