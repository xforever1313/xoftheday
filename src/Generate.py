'''
Copyright Seth Hendrick 2015.
Distributed under the Boost Software License, Version 1.0.
(See accompanying file ../LICENSE_1_0.txt or copy at
http://www.boost.org/LICENSE_1_0.txt)
'''
import argparse
from mysql.connector import (connection)

from Configure import *

class Generator():
    def __init__(self, settings):
        self.settings = settings
        self.db = connection.MySQLConnection(
            user = self.settings['DB_USERNAME'],
            password = self.settings['DB_PASSWORD'],
            host = self.settings['DB_URL'],
            database = self.settings['DB_NAME']
        )

    def __enter__(self):
        return self

    def GetRandomItem(self):
        item = None

        query = "SELECT * FROM " + self.settings['DB_TABLE'] + \
                " WHERE shown=0 ORDER BY RAND() LIMIT 1"

        cursor = self.db.cursor()
        cursor.execute(query)

        hasResult = False

        for (id, content, shown) in cursor:
            hasResult = True
            item = content.replace("\\n", "\n")
            item = '\002' + item + '\003'

            query = "UPDATE " + self.settings['DB_TABLE'] + \
                    " SET shown=1" + \
                    " WHERE id=" + str(id)

            updateCursor = self.db.cursor()
            updateCursor.execute(query)
            updateCursor.close()

        self.db.commit()
        cursor.close()

        return item

    def InsertIntoDatabase(self, text):
        query = ("INSERT INTO " + self.settings['DB_TABLE'] + \
                 " (id, content, shown) " + \
                 "VALUES (NULL, %s, 0)")
        cursor = self.db.cursor()
        cursor.execute(query, (text,))

        self.db.commit()
        cursor.close()

    def RefreshShown(self):
        query = "UPDATE " + self.settings['DB_TABLE'] + \
                " set shown=0"

        cursor = self.db.cursor()
        cursor.execute(query)

        self.db.commit()
        cursor.close()

    def WriteItemToFile(self, item,outFile):
        file = open(outFile, 'w')
        file.write(item)
        file.close()

    def __exit__(self, type, value, traceback):
        if ( self.db != None ):
            self.db.close()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser( description="Reads a random something from the database and writes it to the given file." )
    argParser.add_argument("outfile", action = "store", default="index.html", help="The file to export to.")
    args = argParser.parse_args()

    with Generator(SETTINGS) as generator:
        item = generator.GetRandomItem()

        if (item == None):
            print ("No items returned, resetting shown status...")
            generator.RefreshShown()
            print ("Trying to get new item...")
            item = generator.GetRandomItem()

        if (item == None):
            print ("No items in database.")
            exit(0)

        generator.WriteItemToFile(item, args.outfile)

        print ("Done!")

