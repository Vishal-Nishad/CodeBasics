import pytest
from database import CustomerDB

@pytest.fixture
def db():
    db_instance=CustomerDB()
    db_instance.connect()
    yield db_instance

    db_instance.clear_customers()
    db_instance.close()

def test_insert_customer(db):
    db.insert_customer("vishal","v@gmail.com")
    customer=db.get_customer_by_name("vishal")

    assert customer is not None
    assert customer["name"]=="vishal"
    assert customer["email"]=="v@gmail.com"

def test_get_all_customer(db):
    db.insert_customer("nishad","ncom")
    db.insert_customer("rahul","rahcom")

    customers=db.get_all_customers()
    assert len(customers)==2
