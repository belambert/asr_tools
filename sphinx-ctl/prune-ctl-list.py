#!/usr/bin/python

import sys
import os

if len(sys.argv) != 3:
    print "Usage: %s <ctl file> <directory>"%sys.argv[0]
    exit(-1)

ctl_file = sys.argv[1]
dir=sys.argv[2]
ids = {}

files = os.listdir(dir)

for line in open(ctl_file):
    line = line[:-1]
    ids[line] = True

files = map(lambda x: x[0:-4], files)
file_table = {}

for file in files:
    file_table[file] = True

files_not_found = []

for id in ids.keys():
    if id not in file_table:
        files_not_found.append(id)
    else:
        #pass
        print id

print "%d files in directory"%len(files)
print "%d files in ctl file"%len(ids)
print "%d files not found"%len(files_not_found)
