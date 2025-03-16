balance =0
class InsufficientFunds(Exception):
    pass
def deposit(amount):
    global balance
    if amount<=0:
        raise ValueError("Amount must be in Positive value.")
    balance +=amount
def withdraw(amount):
    global balance
    if amount>balance:
        raise InsufficientFunds(f"Not enough funds. Your current balance is {balance}")

    balance-=amount
deposit(90)
deposit(20)
deposit(9)
withdraw(1110)

print(balance)