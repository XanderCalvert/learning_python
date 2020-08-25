username = input("Username:")
password = input("Password:")

password_length = len(password)
hidden_password = '*' * len(password)

print(f"Hi {username}, your password {hidden_password} is {password_length} characters long.")
