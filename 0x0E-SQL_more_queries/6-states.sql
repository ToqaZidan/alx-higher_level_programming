-- Script that creat database hbtn_0d_usa in your MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- craet table states in the database.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE  NOT NULL AUTO_GENERATE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);