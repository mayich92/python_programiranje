alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26 slova (indeksi 0-25)

# Vigenere
# # ulaz AAABBB, pomak ABC, izlaz ABCBCD

def encrypt_letter(input_letter, direction, shift):
    input_letter_index = alphabet.index(input_letter)
    if direction == 'R':
        output_letter_index = input_letter_index + shift
    elif direction == 'L':
        output_letter_index = input_letter_index - shift
    output_letter_index = output_letter_index % len(alphabet)
    output_letter = alphabet[output_letter_index]
    return output_letter

def caesar_encrypt_text(input_text, direction, shift):
    output_text = ''
    for c in input_text:
        new_letter = encrypt_letter(c, direction, shift)
        output_text += new_letter
    return output_text

# # print(encrypt_text('DOMAGOJ', 'R', 'BC'))
# codeword = 'EEF'
# shift_list = [alphabet.index(c) for c in codeword]
# # shift_list = []
# # for c in codeword:
# #     shift_list.append(alphabet.index(c))
# input_word = 'DOMAGOJ'
# for i, c in enumerate(input_word):
#     print(shift_list[i % len(shift_list)], c)
# print(shift_list)    # modulo?

def vigenere_encrypt_text(input_text, direction, codeword):
    # input_text = input_text.replace(' ')
    # import re
    # input_text = re.sub('[^A-Z]', '', input_text)
    shift_list = [alphabet.index(c) for c in codeword]
    period = len(shift_list)    # len(codeword)
    output_text = ''
    for i, c in enumerate(input_text):
        # if c not in alphabet:
        #     continue
        aligned_index = i % period
        shift = shift_list[aligned_index]
        new_letter = encrypt_letter(c, direction, shift)
        output_text += new_letter
    return output_text

# ulaz AAABBB, pomak ABC, izlaz ABCBCD
encrypted = vigenere_encrypt_text('DOMAGOJ MARIC', 'R', 'EEF')
print(encrypted)