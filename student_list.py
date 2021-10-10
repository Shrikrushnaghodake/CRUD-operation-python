import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="rooy",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM STUDENT")

myresult = mycursor.fetchall()