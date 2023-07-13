import hashlib
import getpass
import json

# Constants for file paths
USERS_FILE = "users.json"
PASSWORDS_FILE = "passwords.json"

# Global variables to store user and password data
users = {}
passwords = {}


def load_data():
    global users, passwords

    try:
        with open(USERS_FILE, "r") as users_file:
            users = json.load(users_file)
    except FileNotFoundError:
        users = {}

    try:
        with open(PASSWORDS_FILE, "r") as passwords_file:
            passwords = json.load(passwords_file)
    except FileNotFoundError:
        passwords = {}


def save_data():
    with open(USERS_FILE, "w") as users_file:
        json.dump(users, users_file)

    with open(PASSWORDS_FILE, "w") as passwords_file:
        json.dump(passwords, passwords_file)


def create_account():
    print("\nCreate Account")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    # Hash the password using SHA256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Store the hashed password in the users dictionary
    users[username] = hashed_password
    passwords[username] = {}

    save_data()
    print("Account created successfully!")


def login():
    print("\nLogin")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    hashed_password = users.get(username)

    if not hashed_password:
        print("Invalid username or password.")
        return None

    # Hash the provided password and compare it with the stored hashed password
    entered_password = hashlib.sha256(password.encode()).hexdigest()

    if entered_password == hashed_password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None


def add_password(username):
    print("\nAdd Password")
    account = input("Enter account name: ")
    password = getpass.getpass("Enter password: ")

    if account in passwords[username]:
        print("Account already exists. Please choose a different account name.")
        return

    # Store the password in the passwords dictionary for the respective user
    passwords[username][account] = password

    save_data()
    print("Password added successfully!")


def view_passwords(username):
    print("\nView Passwords")
    user_passwords = passwords.get(username)

    if not user_passwords:
        print("No passwords found for this user.")
        return

    print("Passwords:")
    for account, password in user_passwords.items():
        print(f"Account: {account}, Password: {password}")


def main():
    load_data()

    while True:
        print("\nPassword Manager")
        print("1. Create Account")
        print("2. Login")
        print("3. Add Password")
        print("4. View Passwords")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            logged_in_user = login()
            if logged_in_user:
                print(f"Logged in as {logged_in_user}")
        elif choice == "3":
            if logged_in_user:
                add_password(logged_in_user)
            else:
                print("Please login first.")
        elif choice == "4":
            if logged_in_user:
                view_passwords(logged_in_user)
            else:
                print("Please login first.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    save_data()


if __name__ == "__main__":
    main()
