import pandas as pd
import numpy as np
import os

def create_synthetic_network_data(num_samples=5000):
    np.random.seed(42)
    
    # 1. Normal Traffic (Label: 0)
    normal_samples = int(num_samples * 0.7)
    normal_data = pd.DataFrame({
        'packet_size': np.random.normal(500, 100, normal_samples),
        'duration': np.random.normal(0.5, 0.1, normal_samples),
        'failed_logins': np.zeros(normal_samples),
        'connection_rate': np.random.normal(10, 2, normal_samples),
        'label': 0 # Benign
    })
    
    # 2. DoS Attack Traffic (Label: 1) - High connection rate
    dos_samples = int(num_samples * 0.15)
    dos_data = pd.DataFrame({
        'packet_size': np.random.normal(1000, 200, dos_samples),
        'duration': np.random.normal(10.0, 2.0, dos_samples),
        'failed_logins': np.zeros(dos_samples),
        'connection_rate': np.random.normal(500, 50, dos_samples),
        'label': 1 # Malicious
    })
    
    # 3. Brute Force Attack (Label: 1) - High failed logins
    brute_samples = int(num_samples * 0.15)
    brute_data = pd.DataFrame({
        'packet_size': np.random.normal(200, 50, brute_samples),
        'duration': np.random.normal(2.0, 0.5, brute_samples),
        'failed_logins': np.random.randint(5, 50, brute_samples),
        'connection_rate': np.random.normal(5, 1, brute_samples),
        'label': 1 # Malicious
    })
    
    # Combine and shuffle
    df = pd.concat([normal_data, dos_data, brute_data]).sample(frac=1).reset_index(drop=True)
    
    # Ensure data folder exists
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/network_traffic.csv', index=False)
    print(f"✅ Generated {len(df)} simulated network records in data/network_traffic.csv")

if __name__ == "__main__":
    create_synthetic_network_data()