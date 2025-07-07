import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def optimize_decision_tree(X, y):
    
    # Hiperparametre grid tanımla
    param_grid = {
        'max_depth': [3, 5, 7, 10],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 5]
    }

    grid_search = GridSearchCV(
        estimator=DecisionTreeClassifier(random_state=42),
        param_grid=param_grid,
        scoring='accuracy',
        cv=5,
        verbose=1
    )
    grid_search.fit(X, y)

    # En iyi parametreleri döndür
    best_params = grid_search.best_params_
    return best_params

def train_optimized_decision_tree(X, y, best_params):
    
    # Eğitim ve test setlerine ayır---  %10-->train   %90--->test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    # Yeni model oluştur ve test için eğit
    model = DecisionTreeClassifier(random_state=42, **best_params)
    model.fit(X_train, y_train)
    print("Decision Tree modeli başarıyla eğitildi.")

    # Test seti üzerinde tahmin yap
    y_pred = model.predict(X_test)

    # Performans metriklerini hesapla
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Doğruluk Oranı (Accuracy): {accuracy}")
    print("\nSınıflandırma Raporu:")
    print(classification_report(y_test, y_pred))

    # Confusion matrix
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    return X_test, y_test, y_pred
