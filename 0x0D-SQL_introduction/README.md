# 0x0D. SQL - Introduction

## Description
This project is focused on understanding and applying SQL concepts using MySQL. The tasks involve creating, manipulating, and querying databases and tables to solidify the fundamentals of SQL and relational databases.

## Learning Objectives
By the end of this project, you should be able to explain and demonstrate:
- What a database is
- The concept of a relational database
- The meaning and purpose of SQL and MySQL
- How to create and manage databases and tables
- How to use DDL (Data Definition Language) and DML (Data Manipulation Language)
- How to perform `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations
- The usage of subqueries and MySQL functions

## Requirements
- All SQL queries should be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- All scripts should have comments describing the task they perform.
- All SQL keywords should be in uppercase.
- The files must end with a new line and be checked with `wc`.
- The use of `SELECT` or `SHOW` statements is restricted in specific tasks.

## Installation
### MySQL Installation on Ubuntu 20.04
```bash
sudo apt update
sudo apt install mysql-server
mysql --version  # Verify the installation
```

### Connect to MySQL
```bash
sudo mysql
```

## File Descriptions

### Mandatory Tasks
- **0-list_databases.sql**: Script that lists all databases on the MySQL server.
- **1-create_database_if_missing.sql**: Script that creates the database `hbtn_0c_0`.
- **2-remove_database.sql**: Script that deletes the `hbtn_0c_0` database.
- **3-list_tables.sql**: Script that lists all tables in a specified database.
- **4-first_table.sql**: Script that creates a table called `first_table` in the current database.
- **5-full_table.sql**: Script that displays the full description of `first_table`.
- **6-list_values.sql**: Script that lists all rows of `first_table`.
- **7-insert_value.sql**: Script that inserts a new row into `first_table`.
- **8-count_89.sql**: Script that counts the number of records with `id = 89` in `first_table`.
- **9-full_creation.sql**: Script that creates `second_table` and inserts multiple rows.
- **10-top_score.sql**: Script that lists all records of `second_table` ordered by `score`.
- **11-best_score.sql**: Script that selects records with `score >= 10` from `second_table`.
- **12-no_cheating.sql**: Script that updates Bob's score to 10.
- **13-change_class.sql**: Script that deletes records with `score <= 5`.
- **14-average.sql**: Script that computes the average score of all records.
- **15-groups.sql**: Script that counts the number of records with the same `score`.
- **16-no_link.sql**: Script that lists records with non-null `name` values.

### Advanced Tasks
- **100-move_to_utf8.sql**: Script that converts the `hbtn_0c_0` database, `first_table`, and the `name` field to UTF8.
- **101-avg_temperatures.sql**: Script that displays the average temperature by city.
- **102-top_city.sql**: Script that lists the top 3 cities' temperatures in July and August.
- **103-max_state.sql**: Script that displays the max temperature by state.

## Usage
Run each script using the following command:
```bash
mysql -hlocalhost -uroot -p < script_name.sql
```
Replace `script_name.sql` with the name of the file you wish to execute.

