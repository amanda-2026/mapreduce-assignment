#!/usr/bin/env python3
# mapper to find non-English words using pyspellchecker

import sys
import re
from spellchecker import SpellChecker

# Date of Birth: April 18 1990

spell = SpellChecker(language='en') 

for line in sys.stdin:
    words = re.findall(r"[a-zA-Z']+", line)
    for w in words:
        
        if not spell.known([w]):
            print(w + "\t1")