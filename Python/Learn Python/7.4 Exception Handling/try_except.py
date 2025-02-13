x= input("Enter a number:")
y = input('Enter a number:')

d=0
try:
    d=int(x)/int(y)
    a='vishal'+50
except ZeroDivisionError as ze:
    print("Exception Occured: ",ze)
except TypeError as te:
    print("Exception Occured: ", te)
print('The value of d is : ', d)