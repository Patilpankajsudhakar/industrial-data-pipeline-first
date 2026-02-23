import pandas as pd
import random
import time
from datetime import datetime
import os

RAW_PATH = r"C:\Users\patil\OneDrive\Documents\Data Engineering\data-platform\raw"

machines = ["M-101", "M-102", "M-103", "M-104"]

def generate_record():
    return {
        "machine_id": random.choice(machines),
        "temperature": round(random.uniform(60, 120), 2),
        "pressure": round(random.uniform(20, 80), 2),
        "vibration": round(random.uniform(0.1, 5.0), 2),
        "status": random.choice(["RUNNING", "STOPPED"]),
        "timestamp": datetime.now()
    }

for _ in range(1):
    data = [generate_record() for _ in range(25)]
    df = pd.DataFrame(data)

    filename = f"machine_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = os.path.join(RAW_PATH, filename)

    df.to_csv(filepath, index=False)

    print(f"Generated: {filename}")

    time.sleep(60)