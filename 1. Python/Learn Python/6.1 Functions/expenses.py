vishal_expenses=[23,53,654,232,454,123]
rahul_expenses=[435,2343,64654,33]

def total_exp(expenses):
    total=0
    for exp in expenses:
        total+=exp
    return total

print(f"total expenses of vishal is : {total_exp(vishal_expenses)}")
print(f"total expenses of rahul is : {total_exp(rahul_expenses)}")
