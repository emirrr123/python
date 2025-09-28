import random

d = "" #devam edermi 
i = 1  #oyun döngüsü için değişken
puan = 0
r= 0 #random sayı oluşturmak için

while d != "h":

    while i <= 3 :
        r = random.randint(0,4)
        
        s = input(f"{i}.tur: birini seçiniz.(taş-kağıt-makas) : ")

        if s == "taş":
            if r != 2:
                puan += 1
            else:
                print("bu tur puan alamadınız.")

        elif s == "kağıt":
            if r != 3:
                puan += 1
            else:
                print("bu tur puan alamadınız.")

        elif s == "makas" :
            if r != 1:
                puan += 1
            else:
                print("bu tur puan alamadınız.")
        i += 1
    print(f"puanınız : {puan}")

    d = input("devam edicekmisiniz(e-h) : ")
    if d == "e":
        puan = 0
        i = 1
        print("***Yeni-Oyun***")
    else :
        print("***Oyun-Bitti***")
        break



    




    
