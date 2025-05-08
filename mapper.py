#!/usr/bin/env python3
import sys

# get all lines from stdin
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(f'{word}\t1')
