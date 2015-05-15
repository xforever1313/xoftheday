'''
 Copyright Seth Hendrick 2015.
 Distributed under the Boost Software License, Version 1.0.
 (See accompanying file ../LICENSE_1_0.txt or copy at
 http://www.boost.org/LICENSE_1_0.txt)
'''
import argparse
import os

def Generate( fileToExport ):
    print( fileToExport )

if __name__ == "__main__":
    argParser = argparse.ArgumentParser( description="Reads a random something from the database and writes it to the given file." )
    argParser.add_argument("outfile", action = "store", default="index.txt", help="The file to export to.")
    args = argParser.parse_args()
    
    Generate( args.outfile )