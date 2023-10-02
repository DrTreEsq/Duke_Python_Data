# Duke_Python_Data

### Course 1: Python and Pandas - complete✅
### Course 2: Linux and Bash - complete✅
### Course 3: SQL - in progress🧑‍💻
### Course 4: Web Dev and Command Line Tools



# to be placed --
##### Create a SQLite Database and Store Data
###### Use the SQLite Operations notebook to connect and create a SQlite database. Go through the cells to create a table and see what happens when you try to create the same table again.

###### Finally populate the database and load data into it, verifying that the data exists.

#### Querying a SQLite Database
##### Use the notebook to create a new databases, populate it with data and query it from Python.
###### Go through all the cells and practice using different SQL statements to filter out the data and get different results.
##### Use different conditions to search for distinct paths, like file names that are partially matched.
###### https://hub.labs.coursera.org:443/connect/sharedqmijvnhg?forceRefresh=false&path=%2Fnotebooks%2Fpython-scripting%2Fquerying-databases.ipynb&isLabVersioning=file-prep


#### Parse HTML with HTMLParser
##### Use the notebook to practice parsing using the HTMLParser llibrary. Go through all the cells to create a class that will parse HTML.
##### Find an alternative way to prevent double entries from showing up in the exercise
* https://hub.labs.coursera.org:443/connect/sharedyhpayeyu?forceRefresh=false&path=%2Fnotebooks%2Fscrapy-xpath%2Fscraping-with-htmlparser.ipynb&isLabVersioning=file-prep

##### Parse HTML and Persist it to a SQLite Database
* Use the provided Jupyter Notebook and go through all the cells.
* Verify that all works by creating a new connection and querying the database.
* Update the wikipedia-demo project and spider to use some of these techniques to persist data. Next, try parsing all the files in the html directory instead of just one and persist all results. Do you think you can parse other information as well?
* Try parsing the height and the results from all the other athletes, not just the top three places
* https://hub.labs.coursera.org:443/connect/sharedlafqeyzo?forceRefresh=false&path=%2Fnotebooks%2Fscrapy-xpath%2Fpersistence.ipynb&isLabVersioning=file-prep

## 40
# Working with VSCode and MySQL
Working from a terminal using command-line tools is very quick and can feel practical when performing certain tasks. However, using a powerful text editor like MySQL is useful when visualizing data and persisting queries accross sessions, databases, and database servers.

This repository and its contents are closely related to the Scripting with Python and SQL for Data Engineering course on coursera. It will assume you are using the VSCode with MySQL container image which has defaults that these examples use, like host, port, and user credentials.

## Connecting to MySQL

There are a few critical things to be aware when connecting to any database server. In the past weeks, you used an _embedded_ database called SQLite. Unlike SQLite, database servers have distinct information required to connect:

* Host
* Port
* Optional SSL certificate

Database servers can _listen_ on a specific address or hostname, and use a particular port to do so. Most commonly, you can use _localhost_ as the host when the database is on the same server as where you are connecting from. For example, if the database is running in your computer, you will probably use _localhost_.

This is, however, not always true. It is entirely possible to configure database servers to _not_ listen to connections on _localhost_ and only use a FQDN (Fully Qualified Domain Name). This is similar to using ports.

For this course, you will be greeted with a VSCode editor in the browser that has some pre-installed extensions that allow you to connect to MySQL which is running on the same host.

1. Click on the File Explorer icon on the left sidebar
1. Find the _MYSQL_ section and click on it
1. Click on the "+" button to create a new connection

Use the following information to complete the prompts:

* Hostname of the database: `localhost`
* MySQL user to authenticate: `root`
* Press Enter and leave the password field blank
* The port number to connect (prepopulated): `3306`
* Press Enter to leave the certificate file path empty


## Running Queries

The default MySQL database server has several databases in it. Use the _mysql_ database from the server list, and right click on it and select _New Query_. A new pane will show up and allow you to create a query.


Use the following query to try it out:

```sql
SELECT * from user;
```

Next, _do not_ click on the _Run_ button. Use the command palette from VSCode to find the _MYSQL: Run MYSql query_ entry. You should get a new pane with results.

Now it is time to run other queries and create a real database with a useful dataset. In VSCode, on the left side bar, find and click the _Source Control_ section to clone a new repository. When prompted use `https://github.com/alfredodeza/vscode-mysql.git` to clone this repo into the lab.

After cloning, open the _sql_scripts_ directory and click on _setup.sql_. That SQL script creates the database and sets up the required table to populate the data. Use the same technique as before to execute the query with the command palette. If the output shows, it should be similar to:

```
[Start] Executing MySQL query...
[Done] Finished MySQL query.
```

With the table created, you can populate it with the rest of the data in the _populate.sql_. Use the same process as before to execute the query.

Verify that your data exists in the table and _ratings_ database by running a `SELECT` statement:

```sql
SELECT * from ratings LIMIT 100;
```

This query is also available in the _sql_script_ directory. Do some data exploration to check the data and get familar with the type of contents you are going to be working with.

## Exporting to CSV

There are several ways to export data. You can use the power of SQL to create a new script and export the fields and data you need into a CSV file.

Find the _export_csv.sql_ file in the _sql_script_ directory and execute it against the database.

What happens if you run it more than once?

Try changing the script to create a CSV file with only the names and ratings instead of including the region.


## Exporting as SQL

Different databases have their own ways of exporting data. In MySQL databases you can use the `mysqldump` utility to export data. Open up a terminal and run the following command:

```
$ mysqldump -u root -p ratings > vscode-mysql/export.sql
```

Remember that the coursera database doesn't have a password for the `root` user. In a real-life scenario, you would have to type a password and perhaps use a specific user instead of using `root`.

Inspect the _export.sql_ file and check its contents. You can use this same file to load data elsewhere. This operation is useful if you are migrating to and from databases or to create a backup.

Note that the SQL file also has instructions on how to re-create the table and database itself, not only the actual data.
 https://hub.labs.coursera.org:443/connect/sharedqvkkwasn?forceRefresh=false&path=%2F%3Ffolder%3D%2Fhome%2Fcoder%2Fvscode-mysql&isLabVersioning=file-prep



## 41
######  https://hub.labs.coursera.org:443/connect/sharedjvqijhze?forceRefresh=false&path=%2F%3Ffolder%3D%2Fhome%2Fcoder%2Fvscode-mysql&isLabVersioning=file-prep
Running Queries Repository
Running Queries
The default MySQL database server has several databases in it. Use the mysql database from the server list, and right click on it and select New Query. A new pane will show up and allow you to create a query.

* Use the following query to try it out:

      SELECT * from user;

Next, do not click on the Run button. Use the command palette from VSCode to find the MYSQL: Run MYSql query entry. You should get a new pane with results.

Now it is time to run other queries and create a real database with a useful dataset. In VSCode, use the file explorer to open the sql_scripts directory and click on setup.sql. That SQL script creates the database and sets up the required table to populate the data. Use the same technique as before to execute the query with the command palette. If the output shows, it should be similar to:

[Start] Executing MySQL query... [Done] Finished MySQL query. 

With the table created, you can populate it with the rest of the data in the populate.sql file. Use the same process as before to execute the query.

Verify that your data exists in the table and ratings database by running a SELECT statement:

SELECT*from ratings LIMIT100;

This query is also available in the sql_script directory. Do some data exploration to check the data and get familiar with the type of contents you are going to be working with.


## 42
###### https://hub.labs.coursera.org:443/connect/sharednkitdtum?forceRefresh=false&path=%2F%3Ffolder%3D%2Fhome%2Fcoder%2Fvscode-mysql&isLabVersioning=file-prep


