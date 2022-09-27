<!-- databases-sql-dbms.md -->

### Database Crash Course

**Overview: SQL, Databases, and Spreadsheets**

* High-level overview of database architecture
* What is a database?
* Where are databases powerful and where are they not?
* What is SQL?

SQL is a programming language used to interact with nearly all relational databases. SQL was first developed at IBM in the 1970s with major contributions from Oracle. Many extensions to SQL have been created since then.

Spreadsheets (such as Microsoft Excel) differ from databases in that spreadsheets were originally designed for one user. They're great for smallers numbers of users who don't need complicated data manipulation. Databases, on the other hand, are designed to hold massive amounts of information and allow multiple users to quickly and securely access and query data with potentially complex logic all in real time.

The strong suit of a database is not storage. It's search functionality. Or more correctly, a database's strength is the search functionality granted to it by a database management system (DMBS).

* **Database management system (DBMS)**: A piece of software that manipulates a database such as SQL, MongoDB, PostgreSQL, MySQL, etc.
* **Structured Query Language (SQL)** is not a programming language in the normal sense. Instead, it's a **decorative, or declarative, programming language**, which means that you simply express what you want done. How it actually happens is not a big concern. A decorative programming language does things and then gives you what you want. Contrast this with a procedural language such as C++ or Python where the programmer writes step-by-step instructions in a program to exactly define _how_ to accomplish a task.

**Relational vs. non-relational database:**

SQL is the standard language for communicating with **relation database management systems (RDBMS)** such as Oracle, Microsoft SQL Server, PostegreSQL, and MySQL.

A **relational database** is structured, meaning the data is organized in tables. Often, the data within the tables of a relational database have relationships with one another, also called dependencies. On the other hand, a **non-relational database** is document-oriented, which means that all of the information gets stored within a single construct, or document, for each item in the database.

SQL databases:

* SQL databases are relational.
* SQL is short for Structured Query language.
* PostgreSQL and MySQL are examples of SQL databases.

NoSQL Databases:

* NoSQL databases are non-relational.
* A NoSQL databases is less structured and less confined in format, thus allowing for more flexibility and adaptability.
* MongoDB is an example of a NoSQL database.

A database contains one or more tables. Tables have named columns with types like "text" or "number". Tables are like pd.DataFrames.

* **Schemas** categorize the tables in a relational database.
* Each row in a table is called a **record** and each column is called a **field**.
* **Metadata** describes the structure of the data itself, such as the field length and datatype. Ex. in a company database the value 6.95 stored in a field is data about the price of a specific product. The information that this is a number data stored to two decimal places and valued in dollars is metadata.

**Primary and composite keys**

Usually in each table, we will have an ID called a **primary key**. The primary key uniquely identifies rows. This is usually a special ID or a name.

We can also create a **composite key**, or composite primary key, which uses a combination of two or more values to identify rows. For example, let's say we're storing IDs for people. People are likely to have matching names, but it is unlikely that people have the same name, height, and address, so we could use these values with a composite key to uniquely identify people.

**SQL Syntax & Structure**

Query : A statement written in SQL, which may include commands and actions. To access records in a table, you send requests in the form of queries.

SQL has 3 categories of syntax terms: identifiers, literals, and keywords.

* **Identifier** (SQLSyntaxTerm): A unique identifier for an element in a database system. If a database contains a table called "Cars", then "Cars" is the identifier.
* **Literal** (SQLSyntaxTerm): A data value.
* **Keyword** (SQLSyntaxTerm): One of the words that has meaning to the system itself, e.g. `SELECT`, `WHERE`, `AND`, `FROM`, etc.

**SELECT statement**

Simple SQL statements to create, modify, and read. Assume that you have two populated SQL databases with some information.

Q: Return all rows from table `aTableName`:

```sql
SELECT * FROM aTableName
```

* `*`: indicates all columns

Q: Return all rows from columns `col1`, and `col2` of table `aTableName`:

```sql
SELECT col1, col2 FROM aTableName
```

Q: Return all rows from table `aTableName` with condition `col1 > 5`.

```sql
SELECT * FROM aTableName
WHERE col1 > 5;
```

* The above code is spread accross two lines. SQL does not worry about line breaks. It only pays attention to semi-colons to end statements. You could even put `SELECT *` on its own line, for instance.
*   If you had a second condition (e.g. `col2 < 4`), you could **filter** for that too using the `AND` statement:

    ```sql
    WHERE <condition1> AND <condition2> 
    ```

To add new items into the database, we use the `INSERT` command. Add 12 to `col1` and "ab" to `col2` of table `aTableName`:

```sql
INSERT INTO aTableName (col1, col2)
VALUES (12, "ab");
```

**Predicates** can be used in cmbination with `SELECT` to limit the number of records retrieved. The default predicate used is `ALL`, meaning the the following two statements are equivalent.

```sql
SELECT col1, col2 
FROM aTable
```

```sql
SELECT ALL col1, col2 
FROM aTable
```

`DISTINCT` is a predicate keyword for returning unique entries.

Q: Return the unique values of column `CarBrand` in the `Cars` table.

```sql
SELECT DISTINCT CarBrand
FROM Cars
```

Q: What happens if you include more than one column after `SELECT DISTINCT`?

`DISTINCT` basically eliminates duplicate values. When you query additional columns, it will return records that are distinct with respect to the each column. For example,

```sql
SELECT DISTINCT FirstName, Role
FROM Coworkers
```

will only discard records that have the same "FirstName" and "Role". If two co-workers have the same first name and different job titles, that counts as a distinct record, so there will be a duplicate entry in the first column.

**TOP (Keyword)**

`TOP` is a predicate keyword used with `SELECT` that returns the first "n" records or the top "n" percent of records. The `TOP` predicate is applied after all other criteria such as joins, other predicates, grouping, and sorts.

Q: Return the first 5 records from the PRODUCTS table (all columns).

```sql
SELECT TOP 5 *
FROM PRODUCTS
```

Q: Return top 8% of users from the CUSTOMERS table, sorted by amount spent. Query the columns, UserID, Plan, and AmountSpent.

```sql
SELECT TOP 8 PERCENT UserID, Plan, AmountSpent
FROM CUSTOMERS
ORDER BY AmountSpent DESC
```

Q: How do you sort a column in ascending order? A: Ascending order is the default order with `ORDER BY`. Only descending order needs a keyword (`DESC`).

Cloze:

* The `ORDER BY` clause goes after the `WHERE` clause at the **end** of the `SELECT` statement.
* You can explicitly specify ascending order with the `ASC` keyword: `ORDER BY col1, col2, ... ASC`.

Note: `TOP` queries with percent don't really make sense without an `ORDER BY` clause.

**WHERE (Keyword)**

Q: Query all columns for all American cities in the "CITY" table with populations larger than 100000. The "CountryCode" for America is "USA". The "CITY" table is described as follows:

![](code/img/2021-08-sql-hackerrank0.png)

```sql
SELECT * 
FROM CITY
    WHERE CountryCode = "USA" 
    AND Population > 100000
```

Q: Return the "ProductName" and "Price" of the top 5% of products in the "PRODUCTS" table. Order by price and only include records with a price greater than 10.

```sql
SELECT TOP 5 PERCENT ProductName, Price
FROM PRODUCTS
WHERE Price > 10
```

**Comparison Operators**

Comparison operators are used to set conditions because they return booleans. Text comparison is alphabetical. Numerical comparison is numerical, and dates are compared chronologically.

Q: Query the "Name" field of the "CUSTOMERS" table filtered by "Country" for customers outside the United States.

```sql
SELECT Name FROM CUSTOMERS
WHERE Country <> "United States"
```

**Logical Operators**

To find records that do not meet a certain condition, use `WHERE NOT [condition]`.

You can use the keywords `AND` and `OR` to combine conditions in a `WHERE` clause.

Q: Query from the "CUSTOMERS" table for companies ("CompanyName") in either New York or New Jersey.

```sql
SELECT CompanyName
FROM CUSTOMERS 
WHERE State = "New York" OR State = "New Jersey"
```

Q: Convert the following Python expression into a SQL clause:

```python
df['Price'] >= 5 & df['Price'] <= 20
```

```sql
WHERE Price BETWEEN 5 AND 20
```

**Wildcard Characters | LIKE**

The underscore, `_`, leaves one wildcard value. The percentage symbol, `%`, is for an arbitrary number of wildcard values.

Q: Query all fields of the "PRODUCTS" table with a 2-digit "Price" that begin with a "9" using a wildcard expression.

```sql
SELECT * FROM PRODUCTS
WHERE Price LIKE "9_"
```

Q: Query all fields of the "PRODUCTS" table with a "Price" that begins with a 9 and ends with a 0, e.g. 90, 900, 9720, etc.

```sql
SELECT * FROM PRODUCTS
WHERE Price LIKE "9%0".
```

Keep in mind that some flavors of SQL use asterisk, `*`, for the percentage symbol wildcard and a question mark for the underscore wildcard.

**Practice Questions from Hackerrank**

Q: CITY is a table with the following fields: ID, Name, CountrCode, District, Population. Query the number of cities with a population larger than 100,000.

```sql
SELECT COUNT(Name) 
FROM CITY 
WHERE Population > 100000
```

Q: CITY is a table with the following fields: ID, Name, CountrCode, District, Population. Query the total population in the "California" district.

```sql
SELECT SUM(Population)
FROM CITY 
WHERE District = "California"
```

Q: Write a minimal example for the syntax of `ORDER BY` in descending order.

```sql
SELECT col0, ...
FROM TableName
ORDER BY col0, ... DESC;
```

Q: Write a minimal example for the syntax of `INSERT INTO`.

```sql
INSERT INTO TableName 
    (col0, ...)
VALUES
    (val0, ...);
    <optional-value-tuples>
```

Q: How can you find null values in a table? A: Use `IS NULL` and `IS NOT NULL` keywords in a conditional expression.

Q: Write a minimal example for the syntax of `IS NULL`.

```sql
SELECT col0, ...
FROM TableName
WHERE col_name IS NULL;
```

Q: Write a minimal example for the syntax of `IS NULL`.

```sql
SELECT col0, ...
FROM TableName
WHERE col_name IS NOT NULL;
```

Q: How can you modify existing records in a table? A: Use the `UPDATE` and `SET` keywords.

Q: Write a minimal example for the syntax of `UPDATE`.

```sql
UPDATE TableName
SET col0 = value0, ...
WHERE <condition>; 
```

Q: Write a minimal example for the syntax of `DELETE`.

```sql
DELETE FROM TableName WHERE <condition>
```

Cloze:

* `MIN()` and `MAX()` accept a column name as an argument. Ex.\
  `SELECT MIN(col_name) FROM TableName`

#### Miscellanous Database Topics

**Databases vs. Spreadsheets**

Example: Suppose you're opening an online specialty cat store. You open a spreadsheet and track name, product, product, date, address, and quantity of items purchased as your variables for bookkeeping. This might work for a while with a small number of customers, products, and addresses listed. However after a while, the online store gets more popular and you run into issues when one customer, Jane Doe, has multiple addresses listed, when different customers share the same name, and in other messy situations. Customers might get mixed up and the wrong products might get sent to the wrong people. How do you resolve this?

Instead of having one spreadsheet, you separate different related information into database **tables**. For the cat store, we might have a "Customers" table, a "Products" table, and an "Orders" table. This separates the data in a much more efficient way. Now, if Jane changes addresses or phone numbers, her contact information simply gets updated in the "Customers" table. The "Product" table can keep track of all cat inventory. Each product will be listed along with its price, quantity, type, and a unique product ID. The "Orders" table would keep track of every sale you make.

You can see that these tables must be connected to one another. It's these connections that form what we call a database. This system is much more scalable and efficient than the spreadsheet, however databases aren't the best for visualizing the connections between tables. It's all in the programming language of the database management system and difficult to see where improvements should be made.

This is where **entity relationship** diagrams (ERDs) come in. These are a way of visualing database structure. Each table is translated into an entity. Columns within each table are listed as **attributes**. In the previous example, the entities were customer, product, and order. The customer table has attributes such as customer ID, name, address, and phone number. The connections between different tables are visualized through **relationship lines**.

**Data persistence**

Persistence in modern English is defined as follows:

1. Continued or prolonged existence of something. Ex. "the persistence of huge environmental problems".
2. Firm or obstinate continuance of a course of action in spite of difficulty or opposition. "Companies must have patience and persistence".

In the context of data storage in computer systems, **persistence refers to a type of storage where data survives after its creation process has ended**. A data store is considered persistent if it writes to non-volatile storage.

Persistence, or the **persistence mechanism**, is also a term used in cyber security. Once malware gains access to a system, it looks to persist within the system. Malware with persistence has more potential to exploit the system and can sometimes continue to act after restarts and reboots. So what then is a persistence layer?

**Persistence layer**: Any software layer that makes it easier for a program to persist its state is generally called a persistence layer. Persistence layers usually do not achieve persistence _directly_ but through the use of an underlying database management system. Persistence layers are also referred to as data access layers.

The persistence layer is usually a relational database in the data access object pattern, but it can be any persistence mechanism using an abstract API. The function os such an API is to hide all of the complexities of performing CRUD (Create, Read, Update, Delete) operations in the underlying storage mechanism from the application.

**Create, Read, Update, Delete (CRUD)**: These are the four basic operations of persistent storage.

**Database management system**: A database management system (DBMS) is a software system that enables users to define, create, maintain, and control access to a database. Examples of DBMS's include MySQL, PostgreSQL, Microsoft SQL Server, and many others.

**Why use a persistence layer?**

Separating data access and the database engine from business/application logic allows you to easily migrate to different storage engines. Isolating the database logic in a single layer makes it easier to replace and modify in the future. In short, persistence layers make maintenance and extension easier.

source: [Oracle. What is a Database?](https://www.oracle.com/database/what-is-database/)

**References**

* Lucidchart, 2018. Database Tutorial for Beginners [\[video\]](https://youtu.be/wR0jg0eQsZA)
* 0612 TV w/ NERDfirst, 2017. A Database Crash Course! [\[video\]](https://youtu.be/0hKmmh\_4t7w)
* Followup tutorial on entity relationship diagrams (ERDs): https://www.youtube.com/watch?v=QpdhBUYk7Kk
* Connolly, Thomas M.; Begg, Carolyn E. (2014). Database Systems – A Practical Approach to Design Implementation and Management (6th ed.). Pearson. ISBN 978-1292061184
* Data access object. [\[Wikipedia\]](https://en.wikipedia.org/wiki/Data\_access\_object#:\~:text=In%20computer%20software%2C%20a%20data,exposing%20details%20of%20the%20database.).
* Persistence (computer science). [\[Wikipedia\]](https://en.wikipedia.org/wiki/Persistence\_\(computer\_science\)#:\~:text=complicated%20to%20debug.-,Persistence%20layers,an%20underlying%20database%20management%20system.).
* https://www.w3schools.com/sql/default.asp

Chapters that look interesting from databases book: Worlds of Database Systems, Relational Model of Data, High-Level Database models, Databse Language SQL, Semistructured Data Model


