# This is a comment. Comments begin with a # sign. Comments are not part of the code
# and are ignored by the python interpreter.

# Description:
# This script will download a bunch of .jpg files from a website. The files will
# be stored in the directory where the script was when it was executed.
#
# Usage:
# (after having installed python) run this script from command line like this:
#
# python download_url_script.py
#
# or (in a windows-like environment) by double clicking on it.
#
# Petar, April 2014, Leuven

import urllib #imports a module called urllib which contains the necessary tools to download

main_url = "http://www.promacedonia.org/bmark/gp/gal/" #this is a string which holds a part of the url that does not change

#for n in range(346,404): 
## n will assume the values 346, 347 ... 403 in this loop
## syntax of urllib.urlretrieve(source_file, target_file)
## str(n) is just a string representation of the number n
## the action of + is to concatenate strings
## thus this will download the files p_0346.jpg, p_0347.jpg, etc.
#    urllib.urlretrieve (main_url+"p_0"+str(n)+".jpg", "./p_0"+str(n)+".jpg") 

name_list = ["p_000_koritsa",
"p_000_sydyrzhanie_1",
"p_000_sydyrzhanie_2",
"p_000_sydyrzhanie_3",
"p_000_sydyrzhanie_4"] #this is a list of "irregular" names

for name in name_list: #this will loop through the five members of list and download them as well
    urllib.urlretrieve (main_url+name+".jpg", "./"+name+".jpg")
