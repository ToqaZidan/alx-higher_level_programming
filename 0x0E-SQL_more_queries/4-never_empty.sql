-- Script that create the table id--not_null.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);