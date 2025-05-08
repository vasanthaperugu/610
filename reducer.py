#!/usr/bin/env python3
import sys

word2count = {}

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t', 1)
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        continue

for word in word2count:
    print(f'{word}\t{word2count[word]}')
