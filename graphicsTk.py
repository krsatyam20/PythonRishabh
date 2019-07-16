#* all class with function

from tkinter import *

rskl=Tk()

#fg forground
'''
btn=Button(rskl, text = "Red", fg = "red")  
btn.pack( side = LEFT)


btn1=Button(rskl, text = "Green", fg = "green")  
btn1.pack( side = RIGHT)


btn2=Button(rskl, text = "Yellow", fg = "yellow")  
btn2.pack( side = TOP)


btn2=Button(rskl, text = "Blue", fg = "blue")  
btn2.pack( side = BOTTOM)

'''

name = Label(rskl,text = "Name").grid(row = 0, column = 0)

e1 = Entry(rskl).grid(row = 0, column = 1)

password = Label(rskl,text = "Password").grid(row = 1, column = 0)  

e2 = Entry(rskl).grid(row = 1, column = 1)  

submit = Button(rskl, text = "Submit").grid(row = 4, column = 0) 


rskl.mainloop()
