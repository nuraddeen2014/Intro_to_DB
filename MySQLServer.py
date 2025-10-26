import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


try:
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )
    print("Database connected successfully")

except Error as e:
    print(f"Connection Error '({e})'")



try:
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE alx_book_store")
    print("Database 'alx_store_created' successfully!")

    
except mysql.connector.Error as e:
    print(f"Databse error: '{e}'")

finally:
    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed")
    
    if connection.is_connected() and cursor:
        connection.close()
        print("Connection closed")