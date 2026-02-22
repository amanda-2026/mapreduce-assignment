# Mapper for counting words
import sys
import re

# Date of Birth: 

for line in sys.stdin:
    words = re.findall(r"[a-zA-Z']+", line.lower())
    for w in words:
        print (w + "\t")