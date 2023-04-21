# Zadatak 19.
# Napisati funkciju koja kao argumente prima imena dva direktorija (source, destination), pa premješta
# sve fajlove iz izvorišnog u odredišni koji su određene ekstenzije

import os
import shutil

def move_files(source_dir, dest_dir, extension):
    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        return 'error'
    if extension.startswith('.'):
        extension = extension[1:]
    all_files = os.listdir(source_dir)
    chosen_files = []
    for file in all_files:
        if file.endswith('.' + extension):
            chosen_files.append(file)
    for file in chosen_files:
        # shutil.move(source_dir + '/' + file, dest_dir + '/' + file)
        src = os.path.join(source_dir, file)
        dest = os.path.join(dest_dir, file)
        shutil.move(src, dest)
        # alternativno:
        # shutil.copy(src, dest)
        # os.remove(src)
    return chosen_files

os.chdir('Datoteke')
rezultat = move_files('izvorisni', 'odredisni', '.txt')
print(rezultat)