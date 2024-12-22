# Python - Object-Relational Mapping (ORM)

## Project Overview
This project introduces the integration of Python programming with relational databases using Object-Relational Mapping (ORM) concepts. By utilizing the MySQLdb and SQLAlchemy modules, the project demonstrates how to interact with MySQL databases, perform CRUD operations, and map database tables to Python objects for seamless manipulation.

## Learning Objectives
At the end of this project, you will be able to:

1. Explain the benefits and limitations of ORM.
2. Connect to a MySQL database using Python.
3. Execute SQL queries with Python using the MySQLdb module.
4. Use SQLAlchemy to abstract database operations through ORM.
5. Map Python classes to MySQL tables with SQLAlchemy.
6. Transition from SQL-based queries to object-based operations.
7. Create and manage a Python virtual environment.

---

## Project Requirements
### General
- All code must run on Ubuntu 20.04 LTS using Python 3.8.5.
- Use MySQLdb version 2.0.x and SQLAlchemy version 1.4.x.
- All scripts must begin with `#!/usr/bin/python3`.
- Your code should adhere to the `pycodestyle` standards (version 2.8.*).
- Include documentation for all modules, classes, and functions.
- All files must be executable.

### Environment Setup
1. Install MySQL 8.0:
   ```bash
   sudo apt update
   sudo apt install mysql-server
   ```

2. Install Python virtual environment and required modules:
   ```bash
   sudo apt install python3.8-venv
   python3 -m venv venv
   source venv/bin/activate
   pip install mysqlclient SQLAlchemy
   ```

3. Verify installations:
   ```bash
   python3 -c "import MySQLdb; print(MySQLdb.version_info)"
   python3 -c "import sqlalchemy; print(sqlalchemy.__version__)"
   ```

---

## Tasks Overview

### Task 0: Get All States
Write a script to list all states from the database `hbtn_0e_0_usa`. Results must be sorted by `states.id`.

**File:** `0-select_states.py`

### Task 1: Filter States
Write a script to list all states with names starting with `N` from the database.

**File:** `1-filter_states.py`

### Task 2: Filter States by User Input
Display all values in the `states` table where `name` matches a user-provided argument.

**File:** `2-my_filter_states.py`

### Task 3: SQL Injection Safe
Rewrite Task 2 to protect against SQL injection using parameterized queries.

**File:** `3-my_safe_filter_states.py`

### Task 4: Cities by States
List all cities from the database `hbtn_0e_4_usa`, joining `states` and `cities` tables.

**File:** `4-cities_by_state.py`

### Task 5: All Cities by State
List all cities of a specific state from the database.

**File:** `5-filter_cities.py`

### Task 6: First State Model
Define a Python class `State` mapped to the `states` table using SQLAlchemy.

**File:** `model_state.py`

### Task 7: All States via SQLAlchemy
List all `State` objects from the database using SQLAlchemy ORM.

**File:** `7-model_state_fetch_all.py`

### Task 8: First State
Print the first `State` object from the database or `Nothing` if the table is empty.

**File:** `8-model_state_fetch_first.py`

### Task 9: Contains `a`
List all `State` objects containing the letter `a`.

**File:** `9-model_state_filter_a.py`

### Task 10: Get a State
Print the `State` object with the name passed as an argument or `Not found` if none exists.

**File:** `10-model_state_my_get.py`

### Task 11: Add a New State
Add a new `State` object with the name "Louisiana" and print its `id`.

**File:** `11-model_state_insert.py`

### Task 12: Update a State
Update the name of the `State` with `id=2` to "New Mexico."

**File:** `12-model_state_update_id_2.py`

### Task 13: Delete States
Delete all `State` objects with names containing the letter `a`.

**File:** `13-model_state_delete_a.py`

### Task 14: Cities in State
Define a `City` class and write a script to list all `City` objects with their corresponding `State`.

**File:** `model_city.py, 14-model_city_fetch_by_state.py`

---

## Advanced Tasks

### Task 15: City Relationship
Improve models to create a relationship between `State` and `City`. Automatically delete cities if their state is deleted.

**File:** `relationship_city.py, relationship_state.py, 100-relationship_states_cities.py`

### Task 16: List Relationship
List all `State` objects and their corresponding `City` objects.

**File:** `101-relationship_states_cities_list.py`

### Task 17: From City
List all `City` objects and their corresponding `State`.

**File:** `102-relationship_cities_states_list.py`

---

## Usage
1. Set up the database using provided SQL files.
2. Execute Python scripts with appropriate arguments:
   ```bash
   ./<script_name>.py <mysql_user> <mysql_password> <database_name>
   ```
3. Review the output for each task.

---

## Repository
- **GitHub Repository:** `alx-higher_level_programming`
- **Directory:** `0x0F-python-object_relational_mapping`

---
