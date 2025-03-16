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
from contextlib import contextmanager


@contextmanager
def get_db_cursor(commit=False):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="vishal",
        database="expense_manager",
        cursorclass=pymysql.cursors.DictCursor    #enable dictionary output , fetch data in dict format
    )

    print("Connection successful")
    cursor = connection.cursor()
    yield cursor
    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:

        cursor.execute("SELECT* FROM expenses")
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)

def insert_expense(expense_date, amount, category,notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category,notes) VALUES (%s,%s,%s,%s)",
            (expense_date,amount,category,notes)
                       )
def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s",(expense_date,))

if __name__=="__main__":
    #fetch_all_records()
    #fetch_expenses_for_date("2024-08-01")
    #insert_expense("2025-08-20",300,"food","Panipuri")
    print("---fetch expense---")
    fetch_expenses_for_date("2025-08-20")
    print("--delete expense--")
    delete_expenses_for_date("2025-08-20")
