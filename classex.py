import random

class Dusman:

    def __init__(self):
        self.durum  = True
        self.saglik = random.randint(50,80)
        self.kalkan = random.randint(5,25)
        self.vurus  = random.randint(20,50)

    def vur(self,o1):
        hasar = self.vurus - o1.kalkan      # düşman vurduğunda vereceği hasar, düşmanın vuruş gücünden oyuncunun kalkan gücünün çıkmasıdır.

        if hasar < 0:                       # eğer kalkanın gücü vuruş gücünden fazlaysa kalkanın gücü düşmeye devam edecek ama hasar 0 olarak kalsın.
            hasar = 0
        
        o1.kalkan -= self.vurus / 10        # oyuncunun kalkan gücü, düşman vurduktan sonra düşmanın vuruş gücunun 1/10 u kadar azalacak.
        o1.kalkan = round(o1.kalkan,2)      # virgülden sonra 2 basamak olması için round fonk. uygulandı.

        if o1.kalkan < 0:                   # kalkan eksilerek 0 ın altına düşerse negatife düşmesin ve 0 olarak sabitlensin.
            o1.kalkan = 0

        o1.saglik -= hasar                  # düşmanın sağlığı, hesaplanan hasar kadar düşecek.
        o1.saglik = round(o1.saglik,2)      # virgülden sonra 2 basamak olması için round fonk. uygulandı.

        if o1.saglik <= 0:                  # oyuncunun sağlığı 0 veya altına düşerse durumu da False olacak yani yenilmiş olacak.
            o1.durum = False
            
class Oyuncu:

    def __init__(self):
        self.durum  = True
        self.saglik = 150
        self.kalkan = 30
        self.vurus  = 55

    def vur(self,d):
        hasar = self.vurus - d.kalkan       # oyuncu vurduğunda vereceği hasar, oyuncunun vuruş gücünden düşmanın kalkan gücünün çıkmasıdır.

        if hasar < 0:                       # eğer kalkanın gücü vuruş gücünden fazlaysa kalkanın gücü düşmeye devam edecek ama hasar 0 olacak.
            hasar = 0
        
        d.kalkan -= self.vurus / 5          # düşmanın kalkan gücü, oyuncu vurduktan sonra oyuncunun vuruş gücunun 1/5 i kadar azalacak.
        d.kalkan = round(d.kalkan,2)        # virgülden sonra 2 basamak olması için round fonk. uygulandı.

        if d.kalkan < 0:                    # kalkan eksilerek 0 ın altına düşerse negatife düşmesin ve 0 olarak sabitlensin.
            d.kalkan = 0

        d.saglik -= hasar                   # oyuncunun sağlığı, hesaplanan hasar kadar düşecek.
        d.saglik = round(d.saglik,2)        # virgülden sonra 2 basamak olması için round fonk. uygulandı.

        if d.saglik <= 0:                   # düşmanın sağlığı 0 veya altına düşerse durumu da False olacak yani yenilmiş olacak.
            d.durum = False
            print("Düşmanı yok ettin")
            dusmanlar.remove(d)             # düşmanın sağlığı bittiğinde listeden silinecek.    
                         
        else:
            print("Düşmanın sağlığı {} kaldı".format(d.saglik))
            secim = d                       # eğer düşmanın sağlığı pozitifse aynı düşman seçimi yenilensin ve tekrardan düşman seçilmesi istenmesin.


o1 = Oyuncu()
dusmanlar = list()

for i in range(10):
    dusmanlar.append(Dusman())              # özellikleri random olarak hesaplanmış 10 tane düşman listeye tanımlanıyor.

secim = -1                                  # oyunun sıfırdan başladığını belirtmesi için

def islem():
    #print("Oyuncu")
    #print(10*"-")
    print("Sağlığın\tKalkanın\tVuruş Gücün")
    print(45*"=")
    print(o1.saglik,"\t\t",o1.kalkan,"\t\t",o1.vurus)
    print(45*"=")
    

    if o1.durum == False:                   # eğer oyuncunun durumu False olursa oyun bitsin.
        print("Game Over")
        quit()
    else:
        count = 0

        for j in dusmanlar:
            count += 1                      # anlık düşman sayısını görebilmek ve mesajlarda yazdırabilmek için sayaç eklendi.

        if secim != -1:                     # eğer oyuncunun durumu True ise ve daha önce seçim yapmış ise kalan sağlık bilgisi ekrana yazdırılsın.
            print("Sağlığın {} kaldı".format(o1.saglik))
        else:
            
            if count == 10:
                print("Oyuna Hoşgeldin. Düşmanlarını aşağıda listeledik.")
            #elif krm == count:
            #    print("Düşman henüz yenilmedi, tekrar saldırabilirsin, ya da başka düşman seçebilirsin.")
            else:
                print("{} tane düşmanınız kaldı. Savaşmaya devam edin.".format(count))
                #oldcount = count

    if not dusmanlar:                       # eğer hiç düşman kalmamışsa mesaj verdirsin ve oyun bitsin.
        print("Tebrikler, tüm düşmanları yok ettin")
        quit()

    print(45*"=")
    #print("Düşmanlar")
    #print(10*"-")
    print("Sağlığı\t\tKalkanı\t\tVuruş Gücü\t Düşman")
    print(60*"=")

    for i in dusmanlar:
        print(i.saglik,"\t\t",i.kalkan,"\t\t",i.vurus,"\t\t","Düşman-{}".format(dusmanlar.index(i)+1))


def boot():
    try:
        gerceksecim = int(input("Yok etmek için bir düşman numarası seç! "))

        if gerceksecim > 0:
            secim = gerceksecim - 1         # listenin index değeri 0 dan başladığı için gerçeksecim den 1 çıkartılır.
            #gerceksecim = secim + 1
            d = dusmanlar[secim]            # seçilen düşmanın indexi d olarak atanır ve classtaki vur fonksiyonlarına yollanır.
            o1.vur(d)
            d.vur(o1)
        else:
            print("Düşman numarası 1 den küçük olamaz!...")
            boot()
    except IndexError:                      # eğer listenin indexleri dışında bir değer girildiyse hata versin.
        print("Olmayan bir duşmanın numarasını seçtiniz. Lütfen düzeltiniz!...")
        boot()                              # tekrar seçim yapmasını istesin.
    except ValueError:                      # eğer rakam/sayı dışında bir değer girildiyse hata versin.
        print("Numara dışında başka bir karakter girdiniz. Lütfen düzeltiniz!...")
        boot()                              # tekrar seçim yapmasını istesin.


while True:
    islem()

    if secim == -1:
        boot()
    else:
        secim = d                           # oyun sıfırdan başlamıyorsa düşmanın indexi secim değeri olarak atanır.
        o1.vur(d)                           # oyuncu düşmana vuruş yapar.

        if d.durum == False:
            secim = -1                      # eğer düşmanın sağlığı 0 veya altına düşerse seçim başa dönsün ve yeni düşman seçilmesi istensin.
        else:
            d.vur(o1)                       # eğer düşmanın sağlığı 0 dan fazlaysa oyuncuya vuruş yapabilsin.