''' program to demonstrate the user is authorized or not based on the username and password '''
username=input("enter your username:")
password=input("enter your password:")
if username=="admin" and password=="admin":
    print("user is authorized")
else:
    print("user is not authorized")