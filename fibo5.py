print  ("@@@@@    @     @@@@  @ ")
print  ("@   @  @   @   @     @ ")
print  ("@@@@@  @ @ @   @@@@  @ ")
print  ("@ @    @   @   @     @ ")
print  ("@   @  @   @   @     @ ")

print("====DERET FIBONACCI====")

kok = int(input("masukkan jumLah bilangan: "))

bil1=int(input("masukkan bilangan kesatu: "))
bil2=int(input("masukkan bilangan kedua: "))
for i in range(kok):
  v=bil1
    
  x = bil1+bil2
  bil1=bil2
  bil2=x
  print(v) 