# Authentication System - Hybrid-Encryption (RSA-AES)


## Introduction
This project implements a hybrid authentication system in Python, combining symmetric and asymmetric encryption methods for enhanced security. User passwords are securely encrypted using symmetric encryption, and the symmetric key is stored securely using asymmetric encryption. The cryptography library is utilized for encryption and decryption operations.

## Encryption Methods Used
- **Symmetric Encryption:** Utilized to encrypt and decrypt user passwords using a shared secret key. Fernet encryption scheme from the cryptography library is employed.
- **Asymmetric Encryption:** Used for securely storing and transmitting the symmetric key. RSA encryption algorithm from the cryptography library is utilized.a

## Prerequisites
Ensure the following dependencies are installed:
- Python (version 3.7 or higher)
- cryptography library

Install the required library using pip:
```
pip install cryptography
```

## Project Overview
### Components:
1. **authentication.py:** Main module implementing the authentication system.
2. **MySQL Database:** Stores user data including usernames, symmetrically encrypted passwords, and asymmetrically encrypted symmetric keys.

## Implementation
### Step 1: Set Up the MySQL Database
Create a MySQL database named `user_authentication_db` with a table named `users` to store user information.

### Step 2: Implement the Hybrid Authentication System
- Create `authentication.py` module with functionalities for user registration and verification using hybrid encryption.
- Follow the provided implementation code to create the authentication system.

## Usage
1. Import the `Authentication` class from `authentication.py`.
2. Create an instance of `Authentication`, passing MySQL database credentials.
3. Register new users using `register_user` method.
4. Verify user credentials using `verify_user` method.
5. Close the database connection using `close_connection` method when done.

## Conclusion
You have successfully implemented a hybrid authentication system combining symmetric and asymmetric encryption methods. Ensure secure handling of sensitive data and follow best practices for application security.

