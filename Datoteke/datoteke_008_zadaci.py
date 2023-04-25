# Zadatak 22
# napisati funkciju koja radi "find and replace" nad spec. tekst. datotekom
# pattern_to_replace, pattern_to_replace_with, input_file, output_file

import os
os.chdir('Datoteke')

import re

def find_and_replace(pattern_to_replace, pattern_to_replace_with, input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as f:
        data = f.read()
    # data = data.replace(pattern_to_replace, pattern_to_replace_with)
    data = re.sub(pattern_to_replace, pattern_to_replace_with, data)
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(data)

phone_number_regex = '(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}'

# find_and_replace('[\d\s]{3,}', '### #### ###', 'ulazna.txt', 'maskirani_brojevi_telefona.txt')
find_and_replace(phone_number_regex, '### #### ###', 'ulazna.txt', 'maskirani_brojevi_telefona.txt')
