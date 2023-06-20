CREATE DATABASE app;
USE app;

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO users(name,email) VALUES('sample','sample@sample.com');
INSERT INTO users(name,email) VALUES('test','test@test.com');
INSERT INTO users(name,email) VALUES('app','app@app.com');

GRANT ALL ON app.* TO test;
