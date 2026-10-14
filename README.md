# Kinkan Sayma 🍊

## 🔴 Canlı Demo
**[kinkan-sayma.onrender.com/docs](https://kinkan-sayma.onrender.com/docs)** — fotoğraf yükle, modeli canlı dene!
> Not: Ücretsiz sunucu boştayken uyur, ilk istek ~50 sn sürebilir.

Görüntüdeki **kinkan (kumquat)** meyvelerini YOLOv8 ile tespit edip **sayan** uçtan uca bir bilgisayarlı görü projesi. Model sıfırdan eğitildi ve FastAPI ile REST servisi olarak sunuldu.

## 🎯 Ne Yapar?
Bir fotoğraf yüklersin, servis içindeki kinkan sayısını döndürür:
`POST /tahmin` → `{"kinkan_sayisi": 18}`

## 📊 Sonuçlar
| Metrik | Değer |
|--------|-------|
| mAP50 | **0.881** |
| Precision | 0.831 |
| Recall | 0.838 |
| mAP50-95 | 0.556 |

- **Model:** YOLOv8n (transfer learning)
- **Veri:** Roboflow Fruit Counting — 382 görsel (281 train / 54 val / 47 test), tek sınıf (`kinkan`)
- **Eğitim:** 60 epoch, GPU (CUDA)

## 🗂️ Proje Yapısı
egit.py # modeli eğitir
tahmin.py # tek görselde kinkan sayar
main.py # FastAPI servisi
model.pt # eğitilmiş model


## 🚀 Çalıştırma

1. Sanal ortam + paketler:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Servisi başlat:
```bash
uvicorn main:app --reload
```

3. Tarayıcıda test et: `http://127.0.0.1:8000/docs`
   → `POST /tahmin` → **Try it out** → bir görsel yükle → **Execute**

## 🧪 Örnek Çıktı
```json
{ "kinkan_sayisi": 18 }
```

## ⚠️ Sınırlamalar
- Veri seti küçük (382 görsel) ve nesneler küçük/yoğun → çok kalabalık sahnelerde sayım hatası olabilir.
- Tek sınıf (kinkan) için eğitildi; başka meyveleri tanımaz.
- Üretim için daha fazla ve çeşitli veriyle yeniden eğitim önerilir.

## 👤 Yazar
Fatih Taşkın — [GitHub](https://github.com/Fatihtsknnn)