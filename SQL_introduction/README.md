# SQL - Introduction

## Concepts
For this project, we expect you to look at this concept:

- Databases

## Resources
Read or watch:

- [What is Database & SQL?](link)
- [Install MySQL (MySQL Server)](link)
- [A Basic MySQL Tutorial](link)
- [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](link)
- [Basic queries: SQL and RA](link)
- [SQL technique: functions](link)
- [SQL technique: subqueries](link)
- [What makes the big difference between a backtick and an apostrophe?](link)
- [MySQL Cheat Sheet](link)
- [MySQL 8.0 SQL Statement Syntax](link)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use MySQL functions

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE…`)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
### Comments for your SQL file:

```bash
cat my_script.sql
 3 first students in the Batch ID=3
 because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$```


### Install MySQL 8.0 on Ubuntu 20.04 LTS:

```bash
Copy code
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$```

Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$```

### Use the sandbox to run MySQL. 
In the container, credentials are `root/root`.
 * Ask for container `Ubuntu 20.04`
 * connect via SSH
 * Or connect via the Web terminal. 
 * In the container, you should start MySQL before playing with it:

```bash
Copy code
$ service mysql start
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$```

In the container, credentials are `root/root`

# Tasks

## 0. List databases (mandatory)
Write a script that lists all databases of your MySQL server.

## 1. Create a database (mandatory)
Write a script that creates the database hbtn_0c_0 in your MySQL server.

## 2. Delete a database (mandatory)
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

## 3. List tables (mandatory)
Write a script that lists all the tables of a database in your MySQL server.

## 4. First table (mandatory)
Write a script that creates a table called first_table in the current database in your MySQL server.

## 5. Full description (mandatory)
Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.

## 6. List all in table (mandatory)
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

## 7. First add (mandatory)
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

## 8. Count 89 (mandatory)
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

## 9. Full creation (mandatory)
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

## 10. List by best (mandatory)
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

## 11. Select the best (mandatory)
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

## 12. Cheating is bad (mandatory)
Write a script that updates the score of Bob to 10 in the table second_table.

## 13. Score too low (mandatory)
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

## 14. Average (mandatory)
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

## 15. Number by score (mandatory)
Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

## 16. Say my name (mandatory)
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

## 17. Go to UTF8 (#advanced)
Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
You need to convert all of the following to UTF8:

## 18. Temperatures #0 (#advanced)
Import in hbtn_0c_0 database this table dump: [download](link)

## 19. Temperatures #1 (#advanced)
Import in hbtn_0c_0 database this table dump: [download](link) (same as Temperatures #0)
Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

## 20. Temperatures #2 (#advanced)
Import in hbtn_0c_0 database this table dump: [download](link) (same as Temperatures #0)
Write a script that displays the max temperature of each state (ordered by State name).