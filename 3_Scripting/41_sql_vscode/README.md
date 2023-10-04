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
