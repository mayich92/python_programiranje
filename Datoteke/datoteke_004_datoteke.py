import os
os.chdir('Datoteke')

f = open('test.txt', 'w')    # w radi overwrite, a dodaje sadržaj na kraj i čuva već postojeći sadržaj
f.write('neki sadrzaj')
f.close()

fh = open('test.txt', 'r')    # alternativno bez 'r' - po defaultu čitanje
data = fh.read()
fh.close()

data += '\n'
data *= 5
data = data.strip()
print(data)

novi_f = open('test2.txt', 'w')
novi_f.write(data)
novi_f.close()


print('-'*50)
filepath = 'primjer_fajla_bez_ekstenzije'
f2 = open(filepath)
print(f2.read())
f2.close()