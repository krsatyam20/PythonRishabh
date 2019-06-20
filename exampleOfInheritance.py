class calculator:
    @staticmethod
    def addition(a ,b):
        c=a+b
        print(c)

    @staticmethod 
    def subtract(a,b):
        c=a-b
        print(c)   


class message(calculator):

    def hello(m):
        print("Hello This is calculator program")

obj= message()
obj.addition(10,20)
obj.hello()
