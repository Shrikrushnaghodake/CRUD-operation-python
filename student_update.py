import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

query = "UPDATE `STUDENT` SET `STUDENT_NAME`='krishna' WHERE `STUDENT_NAME`='shrikrishna'"

mycursor.execute(query)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
