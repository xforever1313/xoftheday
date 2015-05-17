'''
Copyright Seth Hendrick 2015.
Distributed under the Boost Software License, Version 1.0.
(See accompanying file ../LICENSE_1_0.txt or copy at
http://www.boost.org/LICENSE_1_0.txt)
'''

import argparse

from Configure import *
from Generate import *

def InsertFromFile(fileName):
    with Generator(SETTINGS) as gen:

        inFile = open(fileName, 'r')
        for line in inFile:
            gen.InsertIntoDatabase(line)
        inFile.close()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser( 
        description= "Reads a file line by line and inserts " + \
                     "each line to the database (use \\n in the file to do a new line"
    )
    argParser.add_argument(
        "infile",
        action = "store",
        help="The file to read in"
    )

    args = argParser.parse_args()

    InsertFromFile(args.infile)

