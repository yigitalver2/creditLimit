# Kredi Limiti Tahmin Projesi

## **Proje Açıklaması**
Bu proje, müşterilere ait çeşitli özellikler kullanılarak kredi başvurusunun onaylanıp onaylanmayacağını tahmin etmek amacıyla geliştirilmiştir. Python kullanılarak gerçekleştirilen bu proje, veri hazırlama, makine öğrenimi modeli oluşturma ve model performansını değerlendirme adımlarını içermektedir.

---

## **Veri Kullanımı**
- **Veri Seti:** Proje, `data/` klasöründe bulunan `kredi_veriseti_updated_with_features.xlsx` dosyasını kullanır.
- **Veri Bölünmesi:**
  - Veri seti, eğitim ve test setlerine bölünerek kullanılır.
  - **%90 Eğitim / %10 Test:** Veri setinin %90'ı model eğitimi, %10'u ise modelin performansını değerlendirmek için kullanılır.
- **Özellikler:**
  - Kredi miktarı, yaş, ev durumu, alınan kredi sayısı, telefon durumu gibi özellikler kullanılarak kredi başvurusu tahmini yapılır.
  - Kategorik veriler One-Hot Encoding yöntemiyle sayısal değerlere dönüştürülmüştür.

---

## **Proje Yapısı**

```
creditLimit/
├── data/                       # Veri klasörü
│   └── kredi_veriseti_updated_with_features.xlsx  # Güncellenmiş veri seti
├── outputs/                    # Çıktılar klasörü
│   ├── prediction_results.csv  # Tahmin sonuçları
│   
├── src/                        # Kaynak kod klasörü
│   ├── data_preparation.py     # Veri yükleme ve ön işleme
│   ├── model_training.py       # Model eğitimi ve optimizasyon
│   ├── results.py              # Sonuç kaydetme
│   └── main.py                 # Projeyi çalıştıran ana script
├── venv/                       # Sanal ortam
└── requirements.txt            # Bağımlılıkların listesi
```

---

## **Kullanılan Teknolojiler ve Kütüphaneler**

### **Programlama Dili:**
- Python

### **Kütüphaneler:**
- **Pandas:** Veri yükleme ve işleme.
- **Scikit-learn:**
  - Makine öğrenimi modelleri oluşturma ve değerlendirme.
  - GridSearchCV ile model optimizasyonu.
- **Matplotlib ve Seaborn:**
  - Model performansını görselleştirme.
- **Joblib:** Eğitilen modeli kaydetme.

### **Teknolojiler:**
- **Sanal Ortam (venv):** Projenin bağımlılıklarını izole etmek için kullanılır.
- **Excel:** Veri setinin saklanması ve işlenmesi için kullanılır.

---

## **Projenin Çalıştırılması**

### **1. Ortamı Kurun**
- Proje klasörüne gidin ve sanal ortam oluşturun:
  ```bash
  python3 -m venv venv
  ```
- Sanal ortamı etkinleştirin:
  ```bash
  source venv/bin/activate  # macOS/Linux için
  venv\Scripts\activate   # Windows için
  ```
- Gerekli bağımlılıkları yükleyin:
  ```bash
  pip install -r requirements.txt
  ```

### **2. Veri Setini Kontrol Edin**
- `data/` klasöründe `kredi_veriseti_updated_with_features.xlsx` dosyasının bulunduğundan emin olun.

### **3. Projeyi Çalıştırın**
- Ana script'i çalıştırarak modeli eğitin ve test edin:
  ```bash
  python src/main.py
  ```
- Script şu işlemleri gerçekleştirecektir:
  1. Veriyi yükleyip ön işlemeden geçirir.
  2. Optimizasyon yapılmış bir Decision Tree modelini eğitir.
  3. Tahmin sonuçlarını `outputs/prediction_results.csv` dosyasına kaydeder.
  4. Confusion Matrix'i görselleştirir.

---

## **Performans Metrikleri**
- **Doğruluk Oranı:** ~%76.5
- **Sınıflandırma Raporu:**
  - Precision, Recall ve F1-Score değerleri sınıflar bazında sunulmuştur.
- **Confusion Matrix:** Modelin tahmin doğruluğunu görselleştirir.

---


