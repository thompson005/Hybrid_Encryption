create database user_authentication_db;
use user_authentication_db;
 -- Create Course Table
CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password_encrypted BLOB NOT NULL,
                    symmetric_key_encrypted BLOB NOT NULL
                );

CREATE TABLE IF NOT EXISTS user_keys (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    private_key BLOB NOT NULL
                );

Select * from users;
Select * from user_keys;

DROP TABLE users;
DROP TABLE user_keys;

ALTER TABLE users MODIFY symmetric_key_encrypted TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

