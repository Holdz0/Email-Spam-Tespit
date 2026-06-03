# 📧 Email Spam Tespit

Gmail API kullanarak gelen kutusundaki e-postaları okuyup, içerdikleri spam tehdit kelimelerine göre spam olup olmadığını tespit eden Python programı.

> ⚠️ **Mevcut Sürüm:** Alpha v1.0 — Geliştirme aşamasındadır.

---

## 📌 Proje Hakkında

Bu program, Gmail hesabınıza bağlanarak gelen e-postaları otomatik olarak tarar. Her e-postanın içeriğini analiz ederek önceden tanımlanmış spam anahtar kelimeleriyle karşılaştırır ve e-postanın spam olup olmadığını tespit eder. Amaç, kullanıcıyı zararlı veya istenmeyen içeriklerden korumaktır.

---

## 🚀 Özellikler

- **Gmail API entegrasyonu** ile doğrudan Gmail hesabınıza erişim
- Gelen e-postaların içeriklerini otomatik okuma ve analiz etme
- Önceden tanımlanmış **spam tehdit kelime listesi** ile içerik tarama
- E-postaların spam / spam değil olarak sınıflandırılması
- Saf Python ile yazılmış, hafif ve bağımsız yapı

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji / Kütüphane | Amaç |
|-----------------------|------|
| `Python 3` | Ana programlama dili |
| `Gmail API` (Google API Client) | Gmail hesabından e-posta okuma |
| `google-auth` / `google-auth-oauthlib` | OAuth 2.0 kimlik doğrulama |
| `googleapiclient` | Gmail API istemcisi |

---

## 📂 Dosya Yapısı

```
Email-Spam-Tespit/
└── Files/
    ├── main.py (veya spam_tespit.py)   # Ana program — e-posta okuma ve spam tespiti
    ├── credentials.json                 # Google API kimlik bilgileri (kendin oluşturman gerekir)
    └── token.json                       # OAuth oturumu (ilk çalıştırmada otomatik oluşur)
```

> Not: `credentials.json` dosyası Google Cloud Console'dan edinilir ve repoya dahil edilmemiştir.

---

## ⚙️ Kurulum

### 1. Repoyu Klonla

```bash
git clone https://github.com/Holdz0/Email-Spam-Tespit.git
cd Email-Spam-Tespit/Files
```

### 2. Gerekli Kütüphaneleri Kur

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 3. Gmail API Kimlik Bilgilerini Ayarla

1. [Google Cloud Console](https://console.cloud.google.com/) adresine git
2. Yeni bir proje oluştur
3. **Gmail API**'yi etkinleştir
4. **OAuth 2.0 İstemci Kimliği** oluştur (Uygulama türü: Masaüstü)
5. İndirilen JSON dosyasını `credentials.json` olarak `Files/` klasörüne koy

---

## ▶️ Kullanım

```bash
python main.py
```

İlk çalıştırmada bir tarayıcı penceresi açılır ve Gmail hesabına erişim için izin istenir. İzin verildikten sonra `token.json` dosyası oluşturulur ve program e-postalarını taramaya başlar.

---

## 🔍 Spam Tespiti Nasıl Çalışır?

Program, her e-postanın konu ve içeriğini okuyarak önceden tanımlanmış bir **spam anahtar kelime listesiyle** karşılaştırır. Eşleşen kelime bulunursa e-posta **SPAM** olarak işaretlenir, bulunmazsa **güvenli** olarak kabul edilir.

```
E-posta Alındı
      │
      ▼
İçerik Okundu (Konu + Gövde)
      │
      ▼
Spam Kelime Listesiyle Karşılaştır
      │
   ┌──┴──┐
   │     │
SPAM  Güvenli
```

---

## ⚠️ Önemli Notlar

- Bu proje **Alpha aşamasındadır**; hatalar ve eksiklikler bulunabilir.
- `credentials.json` dosyasını **kesinlikle** repoya ya da halka açık bir yere yükleme.
- Program şu an için yalnızca anahtar kelime tabanlı basit bir tespit yöntemi kullanmaktadır; makine öğrenmesi tabanlı gelişmiş sınıflandırma gelecek sürümlerde eklenebilir.

---

## 🗺️ Gelecek Planlar

- [ ] Spam kelime listesini dışarıdan yapılandırılabilir hale getirme
- [ ] Tespit edilen spam e-postaları otomatik olarak etiketleme veya taşıma
- [ ] Makine öğrenmesi tabanlı sınıflandırma algoritması ekleme
- [ ] Grafik kullanıcı arayüzü (GUI)
- [ ] Birden fazla e-posta hesabı desteği

---

## 📄 Lisans

Bu proje açık kaynaklıdır. Dilediğin gibi kullanabilir ve geliştirebilirsin.
