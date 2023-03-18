# # Napisati program koji kroz konzolu od korisnika prima (cijeli?) broj te ispisuje zbroj znamenki tog broja.
# # Primjer izvođenja:
# Unesite broj: 1798
# Zbroj znamenki je 25

number = input("Unesi jedan cijeli broj: ")
user_list = ([int(num) for num in number])
zbroj_znamenki = 0
for num in user_list:
    zbroj_znamenki += num
print(f"Zbroj znamenki je {zbroj_znamenki}.")



