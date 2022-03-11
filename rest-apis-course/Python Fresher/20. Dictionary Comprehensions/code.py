# ("ID", "USERNAME", "PASSWORD")

users = [
    (0, "Bob", "password"),
    (1, "Jim", "bob123"),
    (2, "Jose", "p4ssw0rd"),
    (3, "username", "h3ll0")
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Login successful!")
else:
    print("Login unsuccessful")