-- Script that creat database hbtn_0d_usa in your MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- craet table states in the database.
CREATE TABLE IF NOT EXISTS 'hbtn_0d_usa'.'states' (
    id INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
);