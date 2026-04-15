import pandas as pd
import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train_and_evaluate():
    print("Loading data...")
    df = pd.read_csv('data/network_traffic.csv')
    
    # Feature Engineering / Splitting
    X = df.drop('label', axis=1)
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training AI Model (Random Forest)...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print("Evaluating Model...")
    predictions = model.predict(X_test)
    
    # Print Metrics
    print("\n--- Classification Report ---")
    print(classification_report(y_test, predictions, target_names=['Benign', 'Malicious']))
    
    # Save Model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/rf_model.pkl')
    print("✅ Model saved to models/rf_model.pkl")
    
    # Generate Confusion Matrix Graphic
    os.makedirs('outputs', exist_ok=True)
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Benign', 'Malicious'], yticklabels=['Benign', 'Malicious'])
    plt.title("Cyber Threat Detection - Confusion Matrix")
    plt.xlabel("AI Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig('outputs/confusion_matrix.png')
    print("✅ Evaluation graph saved to outputs/confusion_matrix.png")

if __name__ == "__main__":
    train_and_evaluate()