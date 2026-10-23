password = input("enter your password : ")

if len(password) < 8:
    print("Weak password -small")
elif password.isalpha():
    print("Weak -only letters")
else:
    print("Strong password - Good job!")
