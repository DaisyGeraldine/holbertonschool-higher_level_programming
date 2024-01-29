# SQL - More queries

## Resources
Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
- [MySQL constraints](https://zetcode.com/mysql/constraints/)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

Extra resources around relational database model design:

- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## More Info
Comments for your SQL file:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```
## Install MySQL 8.0 on Ubuntu 20.04 LTS
NOTE: If you’re using the provided sandbox you don’t need to install MySQL. Skip to the next section.

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

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
$
```

## Use the sandbox to run MySQL
### In the container, credentials are `root/root`

* Ask for container `Ubuntu 20.04`
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:

```bash
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

### In the container, credentials are `root/root`

## How to import a SQL dump
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

# Tasks

## 0. My privileges!
   - **mandatory**
   Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

## 1. Root user
   - **mandatory**
   Write a script that creates the MySQL server user user_0d_1.

## 2. Read user
   - **mandatory**
   Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

## 3. Always a name
   - **mandatory**
   Write a script that creates the table force_name on your MySQL server.

## 4. ID can't be null
   - **mandatory**
   Write a script that creates the table id_not_null on your MySQL server.

## 5. Unique ID
   - **mandatory**
   Write a script that creates the table unique_id on your MySQL server.

## 6. States table
   - **mandatory**
   Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

## 7. Cities table
   - **mandatory**
   Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

## 8. Cities of California
   - **mandatory**
   Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

## 9. Cities by States
   - **mandatory**
   Write a script that lists all cities contained in the database hbtn_0d_usa.

## 10. Genre ID by show
    - **mandatory**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump)
    Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

## 11. Genre ID for all shows
    - **mandatory**
    Import the database dump of hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 10-genre_id_by_show.sql)
    Write a script that lists all shows contained in the database hbtn_0d_tvshows.

## 12. No genre
    - **mandatory**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 11-genre_id_all_shows.sql)
    Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

## 13. Number of shows by genre
    - **mandatory**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 12-no_genre.sql)
    Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

## 14. My genres
    - **mandatory**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 13-count_shows_by_genre.sql)
    Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

## 15. Only Comedy
    - **mandatory**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 14-my_genres.sql)
    Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

## 16. List shows and genres
    - **mandatory**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 15-comedy_only.sql)
    Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

## 17. Not my genre
    - **advanced**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 16-shows_by_genre.sql)
    Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.

## 18. No Comedy tonight!
    - **advanced**
    Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](link_to_dump) (same as 100-not_my_genres.sql)
    Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

## 19. Rotten tomatoes
    - **advanced**
    Import the database hbtn_0d_tvshows_rate dump to your MySQL server: [download](link_to_dump)

## 20. Best genre
    - **advanced**
    Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: [download](link_to_dump) (same as 102-rating_shows.sql)
    Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

## 21. How Do SQL Database Engines Work?
    - **advanced**
    Based on this video:
    You can find here the presentation used in the video.
    Write a blog post to explain to your mother “How Do SQL Database Engines Work?”. Your blog post should contain:
    - an introduction
    - complete explanation
    - examples (not the same as the video)
    - diagrams
    - a summary/conclusion
    Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.
    When done, please add all urls below (blog post, LinkedIn post, etc.)
    Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
