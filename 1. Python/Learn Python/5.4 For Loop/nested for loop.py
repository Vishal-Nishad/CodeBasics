products = ['iphone','ipad','macbook']
regions = ['usa','China','India']
revenue = [20,32,454,14,65,3,43,64,7]

i=0
for pr in products:
    for re in regions:
        rev=revenue[i]
        i+=1
        print(f'{pr} {re} = {rev}')