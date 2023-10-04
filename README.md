# Duke_Python_Data

### Course 1: Python and Pandas - complete✅
### Course 2: Linux and Bash - complete✅
### Course 3: SQL  - complete✅ (cleanup in progress)
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


