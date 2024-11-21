-- This script converts the database, table, and column to UTF8 (utf8mb4) with utf8mb4_unicode_ci collation

-- Ensure the database is explicitly selected
USE hbtn_0c_0;

-- Convert the database to UTF8 (utf8mb4)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF8 (utf8mb4)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the 'name' field to UTF8 (utf8mb4)
ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
