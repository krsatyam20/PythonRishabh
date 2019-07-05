from connection import connection,sqlCommand

con=connection('school')

x=sqlCommand() #call class for execute select query

res=x.all_select_query('teacher') #call function for execute query
rest=con.executeQuery(res) #Execute query and store on rest variable

for x in rest:
    print(x)


tres=x.all_select_query('teacher_address') #call function for execute query
trest=con.executeQuery(tres) #Execute query and store on rest variable

for tx in trest:
    print(tx)
