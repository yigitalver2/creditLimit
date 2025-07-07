import pandas as pd

def load_and_prepare_data():
    
    file_path = "./data/kredi_veriseti_updated_with_features.xlsx"  
    try:
        
        data = pd.read_excel(file_path)
        print("Veri başarıyla yüklendi.")
        print(data.head())  # İlk 5 satır gösterilir

        # Kategorik sütunları sayısal değerlere dönüştür 
        return data
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {file_path}")
        return None

def define_features_and_target(data, target_column):
    
    # Hedef değişken
    y = data[target_column]
    
    # Bağımsız değişkenler (hedef değişken dışındaki sütunlar)
    X = data.drop(columns=[target_column])
    
    print("\nBağımsız Değişkenler (X):")
    print(X.head())
    print("\nHedef Değişken (y):")
    print(y.head())
    
    return X, y
