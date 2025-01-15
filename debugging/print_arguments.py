#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py arg1 arg2 ...")
    sys.exit(1)

for i in range(1, len(sys.argv)):
    print(sys.argv[i])
