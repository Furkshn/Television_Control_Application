import random
import time
class Kumanda():

#                ----------------------------------- Televizyon Kumanda Uygulaması -----------------------------------



    def __init__(self,tv_durum="Kapalı",tv_ses = 0, kanal_listesi = ["Trt"], kanal= "Trt",uygulama = ["Netflix","Youtube","Spotify","Amazon Prime"]):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

        self.uygulama = uygulama

    def tv_aç(self):

        if(self.tv_durum == "Açık"):
            print("Televizyon Zaten Açık !")

        else:
            print("Televizyon Açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı !")
        else:
            print("Televizyon Kapatılıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

         while True:
             cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış: Çıkış")

             if (cevap == "<"):

                 if(self.tv_ses != 0):
                     self.tv_ses -= 1
                     print("Ses:",self.tv_ses)

             elif(cevap == ">"):

                 if(self.tv_ses != 31):
                     self.tv_ses +=1
                     print("Ses:",self.tv_ses)
             else:

                 print("Ses Ayarlandı:",self.tv_ses)
                 break
    def kanal_ekle(self,kanal_ismi):

         print("Kanal Ekleniyor...")
         time.sleep(1)

         self.kanal_listesi.append(kanal_ismi)

    def rastgele_kanal(self):

         rastgele = random.randint(0,len(self.kanal_listesi)-1)

         self.kanal = self.kanal_listesi[rastgele]

         print("Kanal:",self.kanal)

    def __len__(self):
         return len(self.kanal_listesi)

    def __str__(self):

         return "Tv Durumu: {} \nTv Ses: {}\nKanal Listesi: {}\n Şu anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def uygulama_aç(self):

        print("""
        
        Televizyon Uygulamalarından Birini Seçiniz :)
        
        
        ***** Netflix *****      
        
        ----- Youtube -----
        
        ===== Spotify =====
        
        ##### Amazon Prime #####
        
        """)

        app = input("Lütfen İstediğiniz Uygulamayı Seçiniz:")          # Netflix = 1 , Youtube = 2 , Spotify = 3, Amazon Prime = 4

        if(app == "1"):
            time.sleep(1)
            print("Netflix Açılıyor...")
            input("Lütfen İzlemek İstediğiniz İçeriğin Numarasını Giriniz:")
            time.sleep(1)
            print("İyi Seyirler :)")

        elif(app == "2"):
            time.sleep(1)
            print("Youtube Açılıyor...")

        elif(app == "3"):
            time.sleep(1)
            print("Spotify Açılıyor...")
            input("Lütfen Dinlemek İstediğiniz İçeriğin Numarasını Giriniz:")
            time.sleep(1)
            print("Keyifli Dinlemeler :)")

        elif(app =="4"):

            time.sleep(1)
            print("Amazon Prime Açılıyor...")
            input("Lütfen İzlemek İstediğiniz İçeriğin Numarasını Giriniz:")
            time.sleep(1)
            print("İyi Seyirler :)")


kumanda = Kumanda()

print("""
     
     Televizyon Uygulaması
     
     1. Tv Aç
     
     2. Tv Kapat
     
     3. Ses Ayarları
     
     4. Kanal Ekle
     
     5. Kanal Sayısını Öğrenme
     
     6. Rastgele Kanal Geçme
     
     7. Televizyon Bilgileri
     
     8. Uygulama Açma
     
     Çıkmak İçin 'q'ya Basınız...
     

     """)


while True:

    işlem = input("İşlemi Seçiniz:")

    if (işlem =="q"):
        print("Program Sonlandırılıyor...")
        break
    elif (işlem == "1"):
        kumanda.tv_aç()

    elif (işlem =="2"):
        kumanda.tv_kapat()

    elif(işlem =="3"):
        kumanda.ses_ayarları()

    elif(işlem=="4"):
        kanal_isimleri = input("Kanal İsimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(işlem=="5"):

        print("Kanal Sayısı:",len(kumanda))

    elif(işlem=="6"):

        kumanda.rastgele_kanal()

    elif(işlem=="7"):

        print(kumanda)     # Print(Obje) Olunca Str Fonksiyonu Çağırılır.
    elif (işlem =="8"):
        print("Eğlenceli Tv Dünyasına Hoşgeldiniz :)")
        time.sleep(1)

        kumanda.uygulama_aç()
        break

    else:

        print("! Geçersiz İşlem !")











