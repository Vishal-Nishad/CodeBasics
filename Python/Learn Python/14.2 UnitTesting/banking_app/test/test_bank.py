import pytest
from src.bank import BankAccount

def test_create_account():
    account=BankAccount("vishal nishad",100)
    assert account.owner =="vishal nishad"
    assert account.balance == 100

# test for depositing money
def test_deposit():
    account=BankAccount("rahul")
    account.deposit(10)
    account.deposit(20)
    assert account.balance==30

# Test depositing a -ve amt (should raise an error)
    with pytest.raises(ValueError):
        account.deposit(-10)

# Test for withdraw money
def test_withdraw():
    account=BankAccount('ravi',100)
    account.withdraw(40)
    assert account.balance==60

    # test withdrawing more than the balance
    with pytest.raises(ValueError):
        account.withdraw(100)

# Test for checking the balance
@pytest.mark.skip(reason="skippin due to reason")
def test_get_balance():
    account=BankAccount('nisha',200)
    assert account.get_balance()==200