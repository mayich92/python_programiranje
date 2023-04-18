
import re

tekst = '''
Ovo je neki tekst, sadrži brojke 1, 2 i 34. Moji fajlovi su prvi.py, drugi.docx i treci.py.
'''

brojke = re.findall('\d+', tekst)
print(brojke)

fajlovi = re.findall('\w+\.py', tekst)
print(fajlovi)