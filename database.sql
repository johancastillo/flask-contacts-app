/* Dalete Data Base if exists */
DROP DATABASE IF EXISTS flaskcontacts;

/* Create Data Base */
CREATE DATABASE flaskcontacts;
USE flaskcontacts;

/* Definition of the table contacts */
CREATE TABLE contacts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255)
);

/* Inserting data in the table */
INSERT INTO contacts (fullname, phone, email) 
VALUES ("test", "123456", "test@gmail.com");

/* Validations */
SHOW TABLES;
SELECT * FROM contacts;