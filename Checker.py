def check_password(password):
    common = ["123456", "password", "qwerty", "abc123"]
    if password in common:
        return "Very Weak - Common password"
    if len(password) < 8:
        return "Weak - Too short"
    if password.isalpha() or password.isdigit():
        return "Weak - Use mix of letters, numbers, symbols"
    if len(password) >= 12:
        return "Strong - Excellent"
    else:
        return "Medium - Good"

pwd = input("Enter your password: ")
print(check_password(pwd))
