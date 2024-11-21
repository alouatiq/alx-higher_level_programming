-- This script converts the database, table, and column to UTF8 (utf8mb4) with utf8mb4_unicode_ci collation.

-- Select the database to avoid "No database selected" error
USE hbtn_0c_0;

-- Convert the database to UTF8 (utf8mb4) with utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF8 (utf8mb4) with utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the 'name' column to use UTF8 (utf8mb4) with utf8mb4_unicode_ci collation
ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Display the table description to verify changes
SHOW CREATE TABLE first_table;
