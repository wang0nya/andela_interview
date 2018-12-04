import re

# TODO: COMBINE ALL REGEX TO MAKE IT SHORTER -- app2.py

def check_password():
    while True:  
        p = input("Enter password: ")
        if (len(p)<6 or len(p)>12):
            print("Password length has to be between 6 and 12 characters")
            continue
        elif not re.search("[a-z]",p):
            print("Password must have atleast one lower case character")
            continue
        elif not re.search("[0-9]",p):
            print("Password must have atleast one number")
            continue
        elif not re.search("[A-Z]",p):
            print("Password must have atleast one upper case character")
            continue
        elif not re.search("[$#@]",p):
            print("Password must have at least 1 character from [$#@]")
            continue
        else:
            print("Valid Password")
            break

if __name__ == "__main__":
    check_password()