#!/usr/bin/env python3
# reducer for word count

import sys

current = None
count = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue  
    word, c = parts
    c = int(c)

    if word == current:
        count += c
    else:
        if current:
            print(current + "\t" + str(count))
        current = word
        count = c

if current:
    print(current + "\t" + str(count))