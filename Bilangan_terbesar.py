print("Program mencari bilangan terbesar  dari 3 bilangan")

Bil1 = int(input("masukan Bilangan Pertama: "))
Bil2 = int(input("Masukan Bilangan Kedua: "))
Bil3 = int(input("Masukan bilangan Ketiga: "))

if Bil1 > Bil2 > Bil3:
    print("Bilangan Pertama Adalah Bilangan Terbesar",Bil1)
elif Bil2 > Bil3:
    print("Bilangan Kedua Adalah Bilangan Terbesar",Bil2)
else:
    print("Bilangan Ketiga Adalah Bilangan terbesar",Bil3)