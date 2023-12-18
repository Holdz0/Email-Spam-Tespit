def spamtespit():
    with open("spamm.txt","r+",encoding="utf-8") as spamtes:       
        icerik = spamtes.readlines(1)
        a = icerik[0]      
        print(a)
def satır_silici(dosya_adı, satır):
    with open(dosya_adı, 'r', encoding='utf8') as file:
        lines = file.readlines()

    with open(dosya_adı, 'w', encoding='utf8') as file:
        for index, line in enumerate(lines):
            if index != satır - 1:
                file.write(line)


