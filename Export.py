import pandas as pd
import mysql.connector as con
db_name=input("Enter Database Name :  ")
db = con.connect(host="localhost", user="root", password="12345", database=db_name)

query = "SELECT * FROM information"
df = pd.read_sql(query, con=db)

df.to_excel("mysql_data.xlsx", index=False)
print("MySQL data successfully exported to Excel file.")

db.close()
