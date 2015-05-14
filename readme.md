X of the Day
================

X of the day is a simple way to write to a file something of the day.  This can be a quote of the day, a joke of the day, or whatever else you can think of.

Dependencies
====
* Python 2
* Mysql or Mariadb

How it works
==== 
The database table has two columns:

* The first column is the text you want displayed.
* The second column is a boolean value that shows if the thing was displayed yet or not.

Once everything in the database table has been displayed, all would be marked undisplayed.

Whenever Generate.py is ran, it will write to the specified file something that hasn't been shown yet from the database.
It will write out a start character and an end character, that way you can quickly check to make sure a user didn't gain access to the file while it was being written to somehow.  Its written as:
\002Your Something\003

where \002 and \003 are single characters: \002 is the start of text character, and \003 is the end of text character.

Configuring
====
There's a Configure.py.to_configure that you should copy/paste to Configure.py and configure the settings inside.
Since this file probably contains passwords, I strongly recommend you do not commit that file.

