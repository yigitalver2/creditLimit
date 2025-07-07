from data_preparation import load_and_prepare_data, define_features_and_target
from model_training import optimize_decision_tree, train_optimized_decision_tree
from results import save_results, plot_confusion_matrix, plot_classification_report
import os

if __name__ == "__main__":
    # Veriyi yükle ve hazırla
    data = load_and_prepare_data()
    
    if data is not None:
        # Bağımsız ve hedef değişkenleri ayarla
        target_column = "KrediDurumu"
        X, y = define_features_and_target(data, target_column)
        
        # Decision Tree'yi optimize et
        print("\nDecision Tree Optimizasyonu Yapılıyor...")
        best_params = optimize_decision_tree(X, y)
        print(f"En İyi Parametreler: {best_params}")
        
        # Optimize edilmiş modeli test et
        print("\nOptimize Edilmiş Decision Tree Test Ediliyor...")
        X_test, y_test, y_pred = train_optimized_decision_tree(X, y, best_params)
        
        # Tahmin sonuçlarını kaydet
        output_dir = os.path.join(os.path.dirname(__file__), "../outputs")
        os.makedirs(output_dir, exist_ok=True)

        output_csv = os.path.join(output_dir, "prediction_results.csv")
        save_results(y_test, y_pred, output_csv)
        
        # Confusion matrix görselleştir ve kaydet
        cm_path = os.path.join(output_dir, "confusion_matrix.png")
        plot_confusion_matrix(y_test, y_pred, cm_path)

        # Sınıflandırma raporunu görselleştir ve kaydet
        report_path = os.path.join(output_dir, "classification_report.png")
        plot_classification_report(y_test, y_pred, report_path)
        
        print("\nModel test, sonuç kaydetme ve görselleştirme işlemleri tamamlandı.")
