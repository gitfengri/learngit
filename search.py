#!/usr/bin/env python
# encoding:utf-8

import os,sys

def search(path,name):
    result=[]
    for file in os.listdir(path):
        file=os.path.join(path,file)
        if os.path.isfile(file) and name in os.path.split(file)[1]:
            result.append(file)
        if os.path.isdir(file):
            result.extend(search(file,name))
    return result

if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage:path,name"
    else:
        path=os.path.abspath(sys.argv[1])
        name=sys.argv[2]
        print search(path,name)


