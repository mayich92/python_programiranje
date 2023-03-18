# Napisati program koji će uzeti korisnikovu rečenicu kroz konzolu i svaku drugu riječ u toj rečenici preokrenuti
# (te vratiti takav, modificirani string).
# Napomene:
# u ovom primjeru ignorirati potencijalnu interpunkciju
# ostaviti case slova kakav je u originalu (ne pretvarati sve u lower ili upper)
# Primjer izvođenja:
# Unesite rečenicu: the quick brown fox jumps over the lazy dog
# Novi string je:  the kciuq brown xof jumps revo the yzal dog

sentence = input("Unesite rečenicu: ").split()
reversed_word = []
for word in sentence[1::2]:
    indexed_word = sentence.index(word)
    reversed_word = word[::-1]
    sentence[indexed_word] = reversed_word
sentence = " ".join(sentence)
print(sentence)


