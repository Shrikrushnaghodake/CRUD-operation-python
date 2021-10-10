import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE STUDENT (STUDENT_NO INT (3),STUDENT_NAME TEXT (30),STUDENT_DOB DATE,STUDENT_DOJ DATE)")
