def toplama(sayı1,sayı2):
    return int(sayı1) + int(sayı2)

def çıkarma(sayı1,sayı2):
    return int(sayı1 - sayı2)

def çarpma(sayı1,sayı2):
    return int(sayı1 * sayı2)

def bölme(sayı1,sayı2):
    return int(sayı1 / sayı2)


print("***Hesap-Makinesi***")
print("-çıkmak için >esc< yazınız-")

while 1 < 2 :

    sayı1 = input("1.sayıyı giriniz.: ")
    işlem = input("işlemi giriniz(+,-,*,/) :")
    sayı2 = input("2.sayıyı giriniz.: ")

    if işlem == "+":
        print(f"{sayı1} + {sayı2} = {toplama(sayı1,sayı2)}")

    elif işlem == "-":
        print(f"{sayı1} - {sayı2} = {çıkarma(sayı1,sayı2)}")

    elif işlem == "*":
        print(f"{sayı1} * {sayı2} = {çarpma(sayı1,sayı2)}")

    elif işlem == "/":
        print(f"{sayı1} / {sayı2} = {bölme(sayı1,sayı2)}")

    else:
        print("Lütfen var olan işlem parametrelerini seçiniz.")
    
    if str(sayı1) == "esc" or işlem == "esc" or str(sayı2) == "esc":
        print("  ***Hoşça-Kalın***  ")
        print("***Nezir-Emir-ERSÜ***")
        break

