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
        spammail.write(icerik+"\n")

def normalmailler():
    with open("normal_mailler.txt","a",encoding="utf-8")as normalmailler:
        normalmailler.write(icerik+"\n")
def satır_silici(dosya_adı, satır):
    with open(dosya_adı, 'r', encoding='utf8') as file:
        lines = file.readlines()

    with open(dosya_adı, 'w', encoding='utf8') as file:
        for index, line in enumerate(lines):
            if index != satır - 1:
                file.write(line)


   
with open("emailtxt.txt", "r") as emailveri:
    satırlar = emailveri.readlines()
    uzunluk2 = len(satırlar)

    for j in range(1, uzunluk2):
        icerik = satırlar[j - 1]
        uzunluk = len(spamtespit())
        sayac2 = 0

        for k in range(0, uzunluk):
            yazi = spamtespit()[k]
            sayac = icerik.count(yazi)
            sayac2 += 1

            if sayac > 0:
                print("Spam Tespit Edildi")
                spam_mailler()
                satır_silici("emailtxt.txt", j)
                break
            elif sayac2 == uzunluk:
                normalmailler()
                satır_silici("emailtxt.txt", j)
                break

