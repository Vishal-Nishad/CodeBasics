x=input("Enter a number: ")
y=input("Enter a number: ")

d=0
try:
    d=int(x)/int(y)
except Exception as e:
    print("Generic Exception: ",e)