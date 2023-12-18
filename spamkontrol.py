import csv

def csvtotxt():
    with open("CSV_NAME.csv", 'r', newline='', encoding='utf-8') as csv_dosyasi, open("emailtxt.txt", 'w', encoding='utf-8') as txt_dosyasi:
        csv_okuyucu = csv.reader(csv_dosyasi)
        for satir in csv_okuyucu:
            # Her satırı TXT dosyasına yaz
            txt_dosyasi.write(','.join(satir) + '\n')

    print("İşlem tamamlandı.")
csvtotxt()
def spamtespit():
    with open("spamm.txt","r+",encoding="utf-8") as spamtes:       
        icerik = spamtes.read()
        satırlar = icerik.split("\n")       
        return satırlar


def spam_mailler():
    with open("spam_mailler.txt","a",encoding="utf-8")as spammail:
        spammail.write(satir+"\n")

def normalmailler():
    with open("normal_mailler.txt","a",encoding="utf-8")as normalmailler:
        normalmailler.write(satir+"\n")
def satır_silici(dosya_adı, satır):
    with open(dosya_adı, 'r', encoding='utf8') as file:
        lines = file.readlines()

    with open(dosya_adı, 'w', encoding='utf8') as file:
        for index, line in enumerate(lines):
            if index != satır - 1:
                file.write(line)

while True:
   
    with open("emailtxt.txt","r")as emailveri:
        satırlar = emailveri.redlines()
        uzunluk2 = len(satırlar)
        for i in range(1,uzunluk2):
            icerik = emailveri.readlines(i)
            satir = icerik[i-1]
            uzunluk = len(spamtespit())
            sayac2 = 0

            for i in range(0,uzunluk):  
                yazi = spamtespit()[i]
                sayac = satir.count(yazi)
                sayac2 += 1
                if sayac == 1:
                    print("spam")
                    spam_mailler()
                    satır_silici("emailtxt.txt",i)
                    break
                elif sayac2 == 218:
                    normalmailler()
                    satır_silici("emailtxt.txt",i)
                    break
    
        




    
        


      

    
                  


    
    
