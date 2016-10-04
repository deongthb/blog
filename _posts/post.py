#!/usr/local/bin/python3
import sys 
import time
import os

timestr = time.strftime("%Y-%m-%d-")
print (timestr)
title = sys.argv[1]
print (title)
fulltitle = timestr+sys.argv[1]+".md"
print (fulltitle)

os.system("/bin/zsh -i -c 'v "+fulltitle+"'")



