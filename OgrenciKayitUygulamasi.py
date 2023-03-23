
def notHesapla(satir):
    satir = satir[:-1]   #boşluklar yüzünden 
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1= int(notlar[0])
    not2= int(notlar[1])
    not3= int(notlar[2])

    ortalama = (not1+not2+not3)/3
    ortalama = round(ortalama,2)
    if(ortalama >=90 and ortalama <= 100):
        harf = "AA"
    elif(ortalama >=85 and ortalama <= 89):
        harf = "BA"
    elif(ortalama >=80 and ortalama <= 84):
        harf = "BB"
    elif(ortalama >=75 and ortalama <= 79):
        harf = "CB"
    elif(ortalama >=70 and ortalama <= 74):
        harf = "CC"
    elif(ortalama >=65 and ortalama <= 69):
        harf = "DC"
    elif(ortalama >=60 and ortalama <= 64):
        harf = "DD"
    elif(ortalama >=50 and ortalama <= 59):
        harf = "FD"
    else:
        harf = "FF"

    return ogrenciAdi + " : " + str(ortalama) +' | '+ harf + '\n'


def ortalamalariOku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(notHesapla(satir))

    
def notGir():
    ad =input("Öğrenci Adı: ")
    soyad =input("Öğrenci Soyadı: ")
    not1 =input("1.Not : ")
    not2 =input("2.Not : ")
    not3 =input("3.Not : ")

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+' ' +soyad+':' +not1+','+not2+','+not3+'\n')
        
    
def notKayitEt():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(notHesapla(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

dongu=True

while dongu:
    islem= input("1- Notları Oku\n2- Not Gir\n3- Notları Dosyaya Kayıt Et\n4- Çıkış\n")

    match islem :
        case '1':
            ortalamalariOku()
        case '2':
            notGir()
        case '3':
            notKayitEt()
        case '4':
            dongu=False
    

