X of the Day
================

X of the day is a simple way to write to a file something of the day.  This can be a quote of the day, a joke of the day, or whatever else you can think of.

Dependencies
====
* Python
* Mysql or Mariadb

How it works
====
The database table has three columns:

* The first column is the id, which is an int and the primary key.
* The second column is the text you want displayed.
* The third column is a boolean value that shows if the thing was displayed yet or not (0 for not shown yet, 1 if so).

Once everything in the database table has been marked as displayed, all would be marked undisplayed the next day.

Whenever Generate.py is ran, it will write to the specified file something that hasn't been shown yet from the database, and mark that as "shown" in the database.
It will write out a start character and an end character, that way you can quickly check to make sure a user didn't gain access to the file while it was being written to somehow.  Its written as:
\002Your Something\003

where \002 and \003 are single characters: \002 is the start of text character, and \003 is the end of text character.

Configuring
====
There's a Configure.py.to\_configure that you should copy/paste to Configure.py and configure the settings inside.
Since this file probably contains passwords, I strongly recommend you do not commit that file.

The database itself should contain only one table with three columns:
id - an integer that is not nullable, auto increments, and is the primary key.
content - text that will contain what will be displayed to the user
shown - a tiny integer value that is 0 if the context int he row was selected to be shown, else 1 if so.

