'''
 Copyright Seth Hendrick 2015.
 Distributed under the Boost Software License, Version 1.0.
 (See accompanying file ../LICENSE_1_0.txt or copy at
 http://www.boost.org/LICENSE_1_0.txt)
'''
import argparse
from mysql.connector import (connection)
import os

from Configure import *

class Generator():
    def __init__(self, outFile, settings):
        self.outFile = outFile
        self.settings = settings
        self.db = connection.MySQLConnection(
            user = self.settings['DB_USERNAME'],
            password = self.settings['DB_PASSWORD'],
            host = self.settings['DB_URL'],
            database = self.settings['DB_NAME']
        )
        self.curser = None

    def __enter__(self):
        return self

    def GetRandomItem(self):
        query = "SELECT * FROM %s" + \
            " WHERE shown=0 ORDER BY RAND() LIMIT 1"
        
        cursor = self.database.cursor()
        cursor.execute(query, (self.settings['DB_TABLE']))
        print (cursor)

    def __exit__(self, type, value, traceback):
        if ( self.curser != None ):
            curser.close()
        
        if ( self.db != None ):
            db.close()
        

if __name__ == "__main__":
    argParser = argparse.ArgumentParser( description="Reads a random something from the database and writes it to the given file." )
    argParser.add_argument("outfile", action = "store", default="index.txt", help="The file to export to.")
    args = argParser.parse_args()
    
    with Generator(args.outfile, SETTINGS) as generator:
        generator.GetRandomItem()
