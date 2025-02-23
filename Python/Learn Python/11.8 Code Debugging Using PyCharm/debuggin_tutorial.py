def total_price(prices,discount):
    total=0
    for price in prices:
        total+=price
    total-=discount
    return total

if __name__=='__main__':
    total=[11,23,11,4]
    discount=4
    print(f"total price is : ",total_price(total,discount))