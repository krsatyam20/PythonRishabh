import mysql.connector

#connect our database

con=mysql.connector.connect(host="localhost",user="root",password="")
#print(con)

concur=con.cursor()

'''concur.execute("show databases")

for x in concur:
    print(x) '''
    
concur.execute("use rishabh")
#concur.execute("create table student(id int(11) primary key auto_increment,name varchar(55))")
concur.execute("show tables")

for x in concur:
    print(x) 

concur.execute("insert into student(name) values('satyam kumar')")
con.commit()
