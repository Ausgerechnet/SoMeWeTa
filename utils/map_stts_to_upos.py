#!/usr/bin/env python3

import json
import sys

with open("stts_to_upos.json") as f:
    mapping = json.load(f)

for line in sys.stdin:
    if line == "\n":
        print()
        continue
    word, pos = line.rstrip().split("\t")
    print("%s\t%s" % (word, mapping[pos]))
