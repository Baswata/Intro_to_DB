#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust user/password/host as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='moding1997!'  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up and close connections
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    create_database()
