-- Script to create the database 'hbtn_0d_usa' and the table 'states'
-- The database will store state information with 'id' as PRIMARY KEY and 'name' as NOT NULL

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
