#! /usr/bin/python
from os.path import dirname
from os.path import join
from sys import path

if __name__ == "__main__":
    path.append(join(dirname(__file__), "./src"))
    import app
