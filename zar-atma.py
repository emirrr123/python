import random


print("  ***Zar-Atma***  ")
print("***Hoş-Geldiniz***")

def zar():
    sayı = random.randint(1,9)
    print(f"{tur}.zar: {sayı}")

adet = int(input("kaç adet zar atıcaksınız: "))

tur= 1


while tur <= adet :
    
    zar()
    tur += 1




