#!/usr/bin/env python
# -*- coding:utf-8 -*-

def testIO(path):
    try:
        f=open(path,'r')
        print f.read()
    finally:
        if f:
           f.close()

