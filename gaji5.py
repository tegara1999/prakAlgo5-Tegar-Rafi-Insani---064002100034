print  ("@@@@@    @     @@@@  @ ")
print  ("@   @  @   @   @     @ ")
print  ("@@@@@  @ @ @   @@@@  @ ")
print  ("@ @    @   @   @     @ ")
print  ("@   @  @   @   @     @ ")
print('=====HITUNGAN ANGKA=====')

waktu_1=float(input('waktu masuk kerja: '))
gaji = 175000
if waktu_1 >=9.00:
    print('selamat pagi')
if waktu_1 >=14.00:
    print('selamat siang')
    
waktu_2=float(input('waktu selesai kerja: '))
if  waktu_2 >=17.00:
    print('selamat sore')
elif waktu_2 >=18.00:
    print('selamat sore')
elif waktu_2 - waktu_1 >=08.00:
    gaji=gaji
elif waktu_2 - waktu_1 >=08.59:
    sarah = int((waktu_2 - waktu_1)-8)
    gaji2 =((kok)*15000)
    
kok = int((waktu_2 - waktu_1)-8)
gaji2 =((kok)*15000)

print('=====RINCIAN GAJI HARIAN=====')
print(f'waktu kerja      :{int(waktu_2 - waktu_1)} jam ( 09.00 sd 18.00)')
print(f'gaji per harian  :Rp.{gaji}')
print(f'lembur           :Rp.{gaji} ({kok} jam x Rp.15000 )')
print(f'total gaji       :Rp.{(gaji)+gaji2}')
if waktu_2 - waktu_1<9.00:
    print('==========TERIMA KASIH==========')