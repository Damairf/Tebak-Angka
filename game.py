import random


terkecil = 1
terbesar = 100
acak = random.randint(terkecil, terbesar)

print('Permainan tebak angka 1-100')
tebakan = int(input('Silahkan masukkan tebakan anda: '))
while tebakan != acak:
    if tebakan > acak:
        print('Tebakan anda diatas angka. Coba lagi')
    elif tebakan < acak:
        print('Tebakan anda dibawah angka. Coba lagi')
    tebakan = int(input('Masukkan angka: '))
print()
print('Tebakan kamu benar')
print('Angka adalah', acak)
print()
print('Permainan Selesai')