file=None
try:
    file= open("Example.txt",'r')
    content=file.read()
    print(content)
except FileNotFoundError as f:
    print("Error: The file was not found.")
finally:
    if file:
        file.close()

    print("file closed")