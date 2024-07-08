digit = True
password = input("Enter Your Password: ")
if len(password) < 8:
    print("Password is too short")
elif "@" not in password:
    print("Passowrd Doesn't Include @")
elif password[0] == '@':
    print("Password Starts with @")
elif password[-1] == '@':
    print("Password Ends with @")
elif password[0] == password[-1]:
    print("Password Starts and Ends with @")
elif password.lower() in password:
    print("Your Password doesn't Include Capital Letter")
else:
    print("Password is Strong")