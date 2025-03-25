import mysql.connector
import sys
import json

# I want to input the values found in the below blocks
# into BrodyG.
# I also want to empty it at the start if it has any elements
hostname = 'dolphin'
port = 3306
username = 'csci375team6'
password='3jni3edn'
database='csci375team6_povertycalculator'

def connect_to_db():
    connection = mysql.connector.connect(
        host=hostname,
        port=port,
        user=username,
        password=password,
        database=database
    )
  
    
   
    

    if connection.is_connected():
        cursor = connection.cursor()
         # Fetch all records from the income table
        cursor.execute("SELECT * FROM income")
        rows = cursor.fetchall()

            # Print each row
        for row in rows:
            print(row)

        connection.close()
        return "succeeded"
    else:
        print("We are actually not connected")
        return "failed"

if __name__ == '__main__':
    print(connect_to_db())