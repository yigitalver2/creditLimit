import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def save_results(y_test, y_pred, output_path):
    """
    Test setindeki gerçek ve tahmin değerlerini kaydet.
    """
    results = pd.DataFrame({
        'Gerçek Değer': y_test,
        'Tahmin Edilen': y_pred
    })
    results.to_csv(output_path, index=False)
    print(f"Tahmin sonuçları {output_path} dosyasına kaydedildi.")

def plot_confusion_matrix(y_test, y_pred, output_path):
    """
    Confusion matrix'i görselleştir ve kaydet.
    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Red', 'Onay'], yticklabels=['Red', 'Onay'])
    plt.xlabel('Tahmin Edilen')
    plt.ylabel('Gerçek Değer')
    plt.title('Confusion Matrix')
    plt.savefig(output_path)
    print(f"Confusion Matrix {output_path} dosyasına kaydedildi.")
    plt.show()

def plot_classification_report(y_test, y_pred, output_path):
    """
    Precision, Recall, F1-Score metriklerini bar grafiği olarak görselleştir ve kaydet.
    """
    from sklearn.metrics import classification_report
    report = classification_report(y_test, y_pred, output_dict=True)
    metrics_df = pd.DataFrame(report).transpose()
    metrics_df = metrics_df[['precision', 'recall', 'f1-score']].drop('accuracy', errors='ignore')

    metrics_df.plot(kind='bar', figsize=(10, 6))
    plt.title('Precision, Recall ve F1-Score')
    plt.ylabel('Skor')
    plt.xlabel('Sınıflar')
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Sınıflandırma raporu görselleştirme {output_path} dosyasına kaydedildi.")
    plt.show()
