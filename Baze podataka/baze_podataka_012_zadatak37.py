import json
import os
import random
os.chdir('Baze podataka')

german_filename = 'german_english.json'
english_filename = 'english_german.json'

with open(german_filename, 'r', encoding='utf-8') as f:
    german_data = json.load(f)

with open(english_filename, 'r', encoding='utf-8') as f:
    english_data = json.load(f)

def sample_dict(vocab, N):
    new_dict = {}
    src_words = list(vocab.keys())
    chosen_words = random.choices(src_words, k=N)
    for word in chosen_words:
        translation = vocab[word]
        new_dict[word.lower()] = translation.lower()
    return new_dict

print('Dobrodošli u prevoditelj DE->EN!')
while True:
    print('-'*50)
    N = input('Unesite broj riječi koliko želite vježbati: ')
    N = int(N)
    lang = input('Unesite izvorni jezik (DE/EN): ').strip().lower()
    if lang == 'de':
        words = sample_dict(german_data, N)
    elif lang == 'en':
        words = sample_dict(english_data, N)
    else:
        print('Unos jezika neispravan!')
        continue
    correct = 0
    print('-'*50)
    for word in words.keys():
        print('Riječ: ', word)
        user_translation = input('Prijevod: ').strip().lower()
        correct_translation = words[word]
        if user_translation == correct_translation:
            print('Točno! ')
            correct += 1
        else:
            print('Netočno! Točan prijevod: ', correct_translation)
        print('-'*50)
    print('Točnih odgovora: ', correct)
    percentage = round((correct / N) * 100, 2)
    print('Postotak točnosti: {} %'.format(percentage))
    end = input('Želite li igrati opet (DA/NE)?').lower()
    if end == 'ne':
        break
print('Hvala na igranju!')