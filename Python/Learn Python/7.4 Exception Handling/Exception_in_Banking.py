balance =0
def deposit(amount):
    global balance
    if amount<=0:
        raise ValueError("Amount must be in Positive value.")
    balance +=amount
def withdraw(amount):
    global balance
    if amount>balance:
        raise ValueError("Amount must be less than the actual balance in account.")
    balance-=amount
deposit(90)
deposit(20)
deposit(9)
withdraw(110)
print(balance)