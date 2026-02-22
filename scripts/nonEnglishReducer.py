#!/usr/bin/env python3
# reducer to sum word counts

import sys

current = None
count = 0

for line in sys.stdin:
    word, c = line.strip().split("\t")
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