from authentication import Authentication, AuthenticationError

# Initialize the Authentication class
auth = Authentication(
    database_host="localhost",
    database_user="root",
    database_password="root",
    database_name="user_authentication_db",
)

while True:
    print("Choose an action:")
    print("1. Sign up")
    print("2. Log in")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Sign up")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            try:
                auth.register_user(username, password)
                print("Registration successful!")
            except AuthenticationError as e:
                print(f"Registration Error: {e}")

    elif choice == "2":
        print("Log in")
        username = input("Enter your username: ")
        login_password = input("Enter your password: ")

        try:
            auth.verify_user(username, login_password)
            print("Login successful!")
        except AuthenticationError as e:
            print(f"Authentication Error: {e}")

    elif choice == "3":
        print("Exiting the program")
        auth.close_connection()
        break