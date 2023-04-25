
import urllib.request
# from urllib import request
# import urllib

url = "https://www.algebra.hr"
konekcija = urllib.request.urlopen(url)
sadrzaj = konekcija.read().decode()
print(sadrzaj)