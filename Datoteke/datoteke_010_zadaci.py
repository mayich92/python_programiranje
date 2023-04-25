# Zadatak 24.
# učitati sadržaj Hrvatska.txt, zapisati frekvencije pojavljivanja riječi u JSON datoteku, sort abecedno

import os
import string
import re
import json
os.chdir('Datoteke')

filepath = 'Hrvatska.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

wordlist = data.split()
while "===" in wordlist:
    wordlist.remove('===')

symbols = string.punctuation
regex_pattern = f'[{symbols}]'

clean_wordlist = []

for word in wordlist:
    word = word.lower()
    word = re.sub(regex_pattern, '', word)
    if word:
        clean_wordlist.append(word)

counts = {}

for word in clean_wordlist:
    if word in counts.keys():
        continue
    frequency = clean_wordlist.count(word)
    counts[word] = frequency

output_filepath = 'frekvencije.json'
with open(output_filepath, 'w', encoding='utf-8') as f:
    json.dump(counts, f, indent=4, sort_keys=True)

# Sortiranje po vrijednosti
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}    # prekomplicirano, ali može se koristiti
counts = {k:counts[k] for k in sorted(counts, key=counts.get, reverse=True)}    # sortiranje po frekvenciji

# Counter
from collections import Counter
lst = ['bok', 'riječ', 'riječ', 'bok', 'bok', 'test']
c = Counter(lst)
frequencies = dict(c)
frequencies_top = c.most_common()    # prima i argument
frequencies_top_dict = {k:v for k,v in frequencies_top}
print(frequencies_top_dict)