import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password123", database = "testdb")
mycursor = mydb.cursor()

#Create table in db
mycursor.execute("Create table in testdb")
mycursor.execute("Create table employee(name varchar(200), sal int(200)")  #creates table in testdb named employee with fields name and sal

#insert records into table
sqlform = "INSERT INTO employee(name,sal) values(%s,%s)" #sql statement
mycursor = executemany(sqlform, employees)
mydb.commit()

#select * from table
mycursor.execute("SELECT * FROM employee")
mycursor.fetchall()

# Delete records from table
sql = "DELETE FROM employee WHERE name = 'John'"
mycursor.execute(sql)
mydb.commit()




