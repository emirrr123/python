import random

def yt():
    x = random.randint(1,2)
    if a == "tura" :
        if x == 2 :
            print("Kazandınız."),
        else:
            print("Kaybettiniz.")

    elif a == "yazı" :
        if x == 1 :
            print("Kazandınız")
        else: 
            print("Kaybettiniz.")
    else:
        print("Belritilen parametreleri yazınız. ")   

   
while 0 < 1:
    a = input("seçiniz(yazı-tura-çıkış) :")
    yt()

    if a == "çıkış":
        break