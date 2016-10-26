# This will print the names of all the user-created files #included by a file 
# by searching for files in a number of directories obtained from a makefile
#
# (user-created means files #included with "...", as opposed to such
# included with <...>)
#
# (see also the c++ version in ~/Documents/c++_stuff)
#
# Petar 
# July 2014, Leuven

from sys import argv
from os import path

filename = argv[1]


def get_includes(filename, level):
    indent =""
    found = 0
    for i in range(level):
        indent +="\t"
    if level == 0:
        file = open(filename, 'r')
        found = 1
    else:
        for curr_dir in include_dirs:
            #print curr_dir
            if path.exists(curr_dir+"/"+filename):
                file = open(curr_dir+"/"+filename, 'r')
                found = 1
    if found == 1 and (not file.closed):
        file_list =[]
        #print indent, "curr file:", filename
        for line in file:
            if "#include" in line:
                if "//" in line:
                    i=line.find("//")
                    line = line[:i]
                if "#include" in line and not ("<" in line):
                    #print line
                    line = line.lstrip("#include ").rstrip("\n")
                    #print line
                    line = line.lstrip("\" ").rstrip("\" \t")
                    print indent + line
                    file_list.append(line)
                    get_includes(line, level+1)
        
        file.close()
    else:
        print indent, "Could not open ", filename

src_dir = "/Users/fun/Documents/DCAMOMS++/src/"
file = open("/Users/fun/Documents/DCAMOMS++/build/bin/Makefile", 'r')
include_dirs =[]

for line in file:
    if "-I" in line:
        #print ""
        #print line.rstrip("\n \\")
        line = line.lstrip("-I \t")
        line = line.rstrip("\n \\")
        line = line.replace("$(SRC_DIR)", src_dir)
        #line = line.replace("Monte", "Monnnte")
        #print line
        include_dirs.append(line)

file.close()
include_dirs.append("/Users/fun/Documents/DCAMOMS++/build/bin/")
new_include=[]
for dirr in include_dirs:
    if "../.." in dirr:
        dirr = dirr.replace("../..", "/Users/fun/Documents/DCAMOMS++/")
    if "//" in dirr:
        dirr = dirr.replace("//","/")
    new_include.append(dirr)
    #print dirr
include_dirs = new_include

get_includes(filename,0)
