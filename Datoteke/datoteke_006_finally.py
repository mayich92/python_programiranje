
import io
import os
os.chdir('Datoteke')

dodatak = 'neki dodatni sadrzaj'    # probajte zakomentirati ovu liniju


try:
    f = open('test4444.txt', 'r')
    f.write('\n')
    f.write(dodatak)
except io.UnsupportedOperation:
    print('Otvorili ste fajl u krivom načinu')
except Exception as e:
    print('Dogodila se greška!')
    print(e)
else:
    print('Pisanje uspješno!')
finally:
    f.close()