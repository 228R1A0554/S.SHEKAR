import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Shekar1435",database="mydb")
mycurs = mydb.cursor()
result=mycurs.execute("select*from user")
for x in result:

mycurs.execute("CREATE TABLE users (name VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")
mycurs.execute("SHOW TABLES")
sql="INSERT INTO users(name, email, password) values(%s,%s,%s)"
val=("Shekar","shekarsadawar20@gmail.com","Shekar1435")
mycurs.execute(sql,val)
#for table in mycurs:
#print(table)