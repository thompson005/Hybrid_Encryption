from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet
import mysql.connector

class AuthenticationError(Exception):
    pass

class Authentication:
    def __init__(self, database_host, database_user, database_password, database_name):
        self.connection = mysql.connector.connect(
            host=database_host,
            user=database_user,
            password=database_password,
            database=database_name,
        )
        self.create_table()

        # Generate asymmetric keys (RSA)
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

        # Generate symmetric key (Fernet)
        self.symmetric_key = Fernet.generate_key()
        self.symmetric_cipher_suite = Fernet(self.symmetric_key)

    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password_encrypted BLOB NOT NULL,
                    symmetric_key_encrypted BLOB NOT NULL
                )
                """
            )
        self.connection.commit()

    def register_user(self, username, password):
        # Encrypt the symmetric key with the user's public key (asymmetric encryption)
        encrypted_symmetric_key = self.public_key.encrypt(
            self.symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        # Encrypt the user password with the symmetric key (symmetric encryption)
        encrypted_password = self.symmetric_cipher_suite.encrypt(password.encode())

        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password_encrypted, symmetric_key_encrypted) VALUES (%s, %s, %s)",
                (username, encrypted_password, encrypted_symmetric_key),
            )
        self.connection.commit()

    def verify_user(self, username, password):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT password_encrypted, symmetric_key_encrypted FROM users WHERE username = %s", (username,)
            )
            row = cursor.fetchone()
            if row is None:
                raise AuthenticationError("User not found.")
            stored_encrypted_password, stored_encrypted_symmetric_key = row

            # Decrypt the symmetric key with the private key (asymmetric decryption)
            decrypted_symmetric_key = self.private_key.decrypt(
                stored_encrypted_symmetric_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )

            # Use the decrypted symmetric key to decrypt the user password (symmetric decryption)
            decrypted_password = Fernet(decrypted_symmetric_key).decrypt(stored_encrypted_password)

            if decrypted_password == password.encode():
                print("Login successful.")
            else:
                raise AuthenticationError("Invalid password.")

    def close_connection(self):
        self.connection.close()
