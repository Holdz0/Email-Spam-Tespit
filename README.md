# 💻 Fiyat Performans Bilgisayar Bulucu

Bütçene göre Trendyol'daki en iyi fiyat/performans oyuncu dizüstü bilgisayarını otomatik olarak bulan Python uygulaması.

---

## 📌 Proje Hakkında

Bilgisayar almak istiyorsun ama piyasayı araştırmaya vaktın yok mu? Bu uygulama senin yerine Trendyol'u tarar, belirttiğin bütçeye göre listelenen oyuncu dizüstü bilgisayarlarını analiz eder ve donanım özelliklerine göre puanlayarak en iyi fiyat/performans seçeneğini sana sunar.

---

## 🚀 Özellikler

- Trendyol'da **"Oyuncu Dizüstü Bilgisayar"** kategorisini otomatik olarak tarar
- Girdiğin ortalama fiyata göre (**±%10 bütçe aralığı**) ürünleri filtreler
- Her bilgisayarın şu özelliklerini toplar:
  - İşlemci markası ve modeli
  - RAM kapasitesi
  - SSD kapasitesi
  - Ekran kartı modeli
  - VRAM miktarı
  - Ekran yenileme hızı (Hz)
  - Ürün URL'si ve fiyatı
- Toplanan verileri **puanlama algoritmasıyla** değerlendirir
- En yüksek puan alan bilgisayarın Trendyol sayfasını **Microsoft Edge ile otomatik açar**
- Sade ve kullanımı kolay **PyQt5 arayüzü**

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane | Amaç |
|-----------|------|
| `selenium` | Trendyol web scraping (tarayıcı otomasyonu) |
| `PyQt5` | Masaüstü GUI arayüzü |
| `Microsoft Edge WebDriver` | Selenium ile tarayıcı kontrolü |

---

## 📂 Dosya Yapısı

```
Fiyat-Performans-Bilgisayar-Bulucu/
├── arayuz.py              # PyQt5 ile oluşturulmuş grafik arayüz
├── trendyol_datapull.py   # Trendyol scraping ve puanlama motoru
└── data.txt               # Kazanan bilgisayarın URL'sinin kaydedildiği dosya (otomatik oluşur)
```

---

## ⚙️ Kurulum

**1. Gereksinimler**

Python 3.x ve aşağıdaki kütüphanelerin kurulu olması gerekir:

```bash
pip install selenium PyQt5
```

**2. Microsoft Edge WebDriver**

Bilgisayarındaki Edge sürümüyle uyumlu WebDriver'ı indirip PATH'e ekle:  
🔗 https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

**3. Repoyu klonla**

```bash
git clone https://github.com/Holdz0/Fiyat-Performans-Bilgisayar-Bulucu.git
cd Fiyat-Performans-Bilgisayar-Bulucu
```

---

## ▶️ Kullanım

```bash
python arayuz.py
```

1. Uygulama açılır, almayı düşündüğün bilgisayarın **ortalama bütçesini** (₺) gir
2. **"Başlat"** butonuna tıkla
3. Program Trendyol'u otomatik olarak tarar (birkaç dakika sürebilir)
4. Tarama tamamlandığında **"Uygun Bilgisayar Bulundu"** ekranı gelir
5. **"Linki Aç"** butonuna tıklayarak en iyi bilgisayarın sayfasını Edge'de görüntüle

---

## 🔢 Puanlama Sistemi

Her bilgisayar aşağıdaki kriterlere göre puan alır; daha güçlü donanım = daha yüksek puan:

| Kriter | Puan Sıralaması (düşükten yükseğe) |
|--------|-------------------------------------|
| **İşlemci** | AMD Ryzen 5 → AMD Ryzen 7 / Intel i5 → Intel i7 |
| **Ekran Kartı** | Dahili → MX550 → RTX 2050 → RTX 3050 → ... → RTX 4090 |
| **RAM** | 8 GB → 12 GB → 16 GB → ... → 40 GB |
| **VRAM** | Paylaşımlı → 4 GB → 6 GB → 8 GB → 12 GB → 16 GB |
| **SSD** | 256 GB → 500 GB → 512 GB → 1 TB → 2 TB |

---

## ⚠️ Notlar

- Program **Microsoft Edge** ve Edge WebDriver kullandığını varsayar. Farklı bir tarayıcı kullanıyorsan `trendyol_datapull.py` içindeki `webdriver.Edge()` satırlarını güncellemelisin.
- Trendyol'un sayfa yapısı değişirse XPath ifadelerinin güncellenmesi gerekebilir.
- Tarama süresi internet hızına ve Trendyol'un yanıt süresine göre değişir.
- Program çalışırken arka planda bir tarayıcı penceresi açılır; bu beklenen bir davranıştır.

---

## 📄 Lisans

Bu proje açık kaynaklıdır. Dilediğin gibi kullanabilir ve geliştirebilirsin.
