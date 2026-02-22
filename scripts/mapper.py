#!/usr/bin/env python3
# mapper for word count

import sys
import re

# Date of Birth: April 18 1990

for line in sys.stdin:
    words = re.findall(r"[a-zA-Z']+", line.lower())
    for w in words:
        if w:
            print(w + "\t1")