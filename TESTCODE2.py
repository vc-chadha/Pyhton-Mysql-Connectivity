import pandas as pd
import mysql.connector as con

db = con.connect(host="localhost", user="root", password="12345")
print(db, "connection created")

def create_table_and_insert_data():
    cur = db.cursor()
    new1 = input("Enter Database's name: ")
    cur.execute("create database {}".format(new1))
    print("Database Created")
    cur.execute("use {}".format(new1))
    print(new1, " is being used")

    
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS information (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), ContactNumber INT, Email VARCHAR(255))")
    print("Table created successfully")
    
    while True:
        
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        contact_number = int(input("Enter Contact Number: "))
        email = input("Enter Email: ")

        sql = "INSERT INTO information (FirstName, LastName, ContactNumber, Email) VALUES (%s, %s, %s, %s)"
        val = (first_name, last_name, contact_number, email)
        cur.execute(sql, val)
        db.commit()

        print(cur.rowcount, "record inserted.")
        check = input("Type 'QUIT' to stop the code")
        
        if check=='QUIT':
            break
        
        
    

create_table_and_insert_data()


import pandas as pd
import mysql.connector as con

db = con.connect(host="localhost", user="root", password="12345")
print(db, "connection created")

def create_table_and_insert_data():
    cur = db.cursor()
    new1 = input("Enter Database's name: ")
    cur.execute("create database {}".format(new1))
    print("Database Created")
    cur.execute("use {}".format(new1))
    print(new1, " is being used")

    
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS information (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), ContactNumber INT, Email VARCHAR(255))")
    print("Table created successfully")
    
    while True:
        
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        contact_number = int(input("Enter Contact Number: "))
        email = input("Enter Email: ")

        sql = "INSERT INTO information (FirstName, LastName, ContactNumber, Email) VALUES (%s, %s, %s, %s)"
        val = (first_name, last_name, contact_number, email)
        cur.execute(sql, val)
        db.commit()

        print(cur.rowcount, "record inserted.")
        check = input("Type 'QUIT' to stop the code")
        
        if check=='QUIT':
            break
        
        
    

create_table_and_insert_data()







##import pandas as pd
##import mysql.connector as con
##
##def exporting():
##    db_name = input("Enter the database name: ")
##
##    db = con.connect(host="localhost", user="root", password="12345", database=db_name)
##
##    query = "SELECT * FROM information"
##    df = pd.read_sql(query, con=db)
##
##    df.to_excel("mysql_data.xlsx", index=False)
##    print("MySQL data successfully exported to Excel file.")
##
##    db.close()
##
##exporting()





    

