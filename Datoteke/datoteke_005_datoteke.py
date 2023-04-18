
import os
os.chdir('Datoteke')

# f = open('test.txt', 'w')
# f.write('neki sadrzaj')
# f.close()

sadrzaj = 'neki sadrzaj'

with open('test3.txt', 'w') as f:
    f.write(sadrzaj)

with open('test3.txt') as f:
    data = f.read()

print(data)
print(data == sadrzaj == 'neki sadrzaj')