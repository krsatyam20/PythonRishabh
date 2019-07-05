'''
open(mode,path)
    mode
        r :read
            read() => read all file at a time
            readline() => line by line read
            readlines() => line by line read, but line convert into list 
        w :write
         write()
        a :append
            open(path,'a')
            write()

        path(file location with file name)


'''

x=open(r"C:\Users\User\Desktop\Java.advance.txt")
print(x)
#print(x.read())
'''print(x.readline())
print(x.readline())
print(x.readline())
print(x.readline())
'''
#print(x.readlines())
readFileandconvertIntoList=x.readlines()

'''for rf in readFileandconvertIntoList:
    print(rf)'''


#count line     

print(len(readFileandconvertIntoList))

wf=open(r"C:\Users\User\Desktop\output.txt",'w')

wf.write('Hello\n')
wf.write('Hello\n')
wf.write('Hello\n')
wf.write('Hello\n')
wf.write('Hello\n')
wf.write('Hello\n')
wf.write('Hello\n')


wf.close()

'''
count word and char in any file'''

