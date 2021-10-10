import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

query = "DELETE FROM `STUDENT` WHERE STUDENT_NAME='krishna'"
mycursor.execute(query)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")