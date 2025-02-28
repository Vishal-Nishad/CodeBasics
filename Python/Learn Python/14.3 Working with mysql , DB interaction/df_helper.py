'''import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="vishal",
    database="expense_manager"

)

if connection.is_connected():
    print("connection successful")
else:
    print("Failed in connecting to a database")'''

import pymysql

def get_db_cursor():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="vishal",
        database="expense_manager",
        cursorclass=pymysql.cursors.DictCursor    #enable dictionary output , fetch data in dict format
    )

    print("Connection successful")
    cursor = connection.cursor()
    return connection,cursor

def fetch_all_records():
    connection,cursor=get_db_cursor()

    cursor.execute("SELECT* FROM expenses")
    expenses=cursor.fetchall()
    for expense in expenses:
        print(expense)
    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    connection, cursor=get_db_cursor()
    cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
    expenses=cursor.fetchall()
    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()

if __name__=="__main__":
    #fetch_all_records()
    fetch_expenses_for_date("2024-08-01")

