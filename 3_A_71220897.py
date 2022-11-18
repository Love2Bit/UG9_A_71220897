import math
panjang = int(input('Masukan panjang : '))
lebar = int(input('Masukan Lebar : '))
jari = int(input('Masukan jari-jari : '))
setlir = int ((3.14*jari*jari)/2)
ppanjang = int(panjang * lebar)
print('Area tersebut membutuhkan ',math.ceil((setlir + ppanjang)/15), 'kaleng cat')