import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

query = "INSERT INTO `STUDENT` (`STUDENT_NO`, `STUDENT_NAME`, `STUDENT_DOB`, `STUDENT_DOJ`) VALUES ('17', 'shrikrishna', '1996-10-17', '2021-10-20')"
mycursor.execute(query)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
