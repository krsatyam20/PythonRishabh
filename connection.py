import mysql.connector
#print(dir(mysql))
class connection:
    def __init__(self,db):
        self.dbname=db
        self.con=mysql.connector.connect(host="localhost",user="root",password="",database=self.dbname)

        
        

    def executeQuery(self,sql):
        concur=self.con.cursor()
        concur.execute(sql)
        
        return concur

    
class sqlCommand:
    def all_select_query(self,tableName):
        self.tableName=tableName
        sql="select * from "+self.tableName+""
        return sql


    
