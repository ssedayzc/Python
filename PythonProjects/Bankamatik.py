SedaHesap = {
    'ad' : 'Seda Nur Yazıcı',
    'hesapNo' : '1243455',
    'bakiye' : 500,
    'ekHesap' : 1000
}

DogukanHesap = {
    'ad' : 'Doğukan Yazıcı',
    'hesapNo' : '2333847',
    'bakiye' : 7000,
    'ekHesap' : 3000
}

def paraCek(hesap, miktar):
    print(f"\nMerhaba {hesap['ad']},\n")

    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print(f"paranızı alabilirsiniz..\nkalan bakiye : {hesap['bakiye']}\n")

    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullanimi = input("yetersiz bakiye, ek hesap kullanılsın mı E/H ?\n")
            if(ekHesapKullanimi == 'e'):
                print("paranızı alabilirsiniz..\n")
                hesap['ekHesap'] -= (miktar - hesap['bakiye'])
                hesap['bakiye'] = 0
                print(f"kalan bakiye : {hesap['bakiye']}\nek hesap bakiye : {hesap['ekHesap']}")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bakiyeniz bulunmaktadır..\n")
        else:
            print("üzgünüz, bakiye yetersiz..\nbakiye : {hesap['bakiye']}\n")


def paraYatir(hesap,miktar):
    print(f"\nMerhaba {hesap['ad']}, \n")
    ekHesapYatirma = input("ek hesaba mı para yatıracaksınız? E/H")
    if(ekHesapYatirma == 'e'):
        hesap['ekHesap'] += miktar
        bakiyeSorgula(hesap)

    else:
        hesap['bakiye'] += miktar
        bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"hesabınızdaki tutar : {hesap['bakiye']}\nek hesabınızdaki tutar : {hesap['ekHesap']}")







paraCek(SedaHesap,1000)
paraYatir(SedaHesap,200)