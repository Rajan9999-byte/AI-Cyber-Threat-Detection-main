import joblib
import pandas as pd
import time
import random

def simulate_real_time_detection():
    print("Starting Live Threat Detection SOC Monitor...")
    print("Loading AI Engine...\n")
    
    try:
        model = joblib.load('models/rf_model.pkl')
    except:
        print("❌ Model not found! Run train_model.py first.")
        return

    # Simulate 10 live incoming packets
    for i in range(1, 11):
        # Randomly generate either normal or attack parameters
        if random.random() > 0.3:
            # Simulate Normal
            packet = pd.DataFrame({'packet_size': [random.uniform(400, 600)], 'duration': [random.uniform(0.4, 0.6)], 'failed_logins': [0], 'connection_rate': [random.uniform(8, 12)]})
            actual_type = "Normal Request"
        else:
            # Simulate Attack (e.g. Brute Force)
            packet = pd.DataFrame({'packet_size': [random.uniform(100, 300)], 'duration': [random.uniform(1.5, 2.5)], 'failed_logins': [random.randint(10, 40)], 'connection_rate': [random.uniform(2, 6)]})
            actual_type = "Brute Force Attack"

        # AI Prediction
        prediction = model.predict(packet)[0]
        
        print(f"[{time.strftime('%H:%M:%S')}] Incoming Traffic -> PacketSize: {packet['packet_size'].iloc[0]:.0f} | Fails: {packet['failed_logins'].iloc[0]} | ConnRate: {packet['connection_rate'].iloc[0]:.0f}")
        
        if prediction == 1:
            print(f"🚨 ALERT: Malicious activity detected! Blocking IP... (Actual Simulation: {actual_type})\n")
        else:
            print(f"✅ Traffic Cleared. (Actual Simulation: {actual_type})\n")
            
        time.sleep(1.5) # Pause to simulate real-time log reading

if __name__ == "__main__":
    simulate_real_time_detection()