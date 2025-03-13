#!/usr/bin/python3

def read_file(filename=""):
    """read file"""
    with open(filename) as f:
        line = f.read()
        print(line, end="")
