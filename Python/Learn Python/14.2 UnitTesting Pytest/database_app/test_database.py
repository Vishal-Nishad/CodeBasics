import pytest
from database import CustomerDB

def test_insert_customer():
    db=CustomerDB()
    db.connect()

    db.insert_customer("vishal","v@gmail.com")
    customer=db.get_customer_by_name("vishal")

    assert customer is not None
    assert customer["name"]=="vishal"
    assert customer["email"]=="v@gmail.com"

    db.clear_customers()

    db.close()

def test_get_all_customer():
    db=CustomerDB()
    db.connect()

    db.insert_customer("nishad","ncom")
    db.insert_customer("rahul","rahcom")

    customers=db.get_all_customers()
    assert len(customers)==2

    db.clear_customers()
    db.close()