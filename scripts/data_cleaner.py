import pandas as pd
import os
from datetime import datetime

RAW_PATH = r"C:\Users\patil\OneDrive\Documents\Data Engineering\data-platform\raw"
PROCESSED_PATH = r"C:\Users\patil\OneDrive\Documents\Data Engineering\data-platform\processed"
LOG_PATH = r"C:\Users\patil\OneDrive\Documents\Data Engineering\data-platform\logs\data_quality_log.csv"

def clean_file(file):
    df = pd.read_csv(os.path.join(RAW_PATH, file))

    original_count = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Validation rules
    df["quality_flag"] = "GOOD"

    df.loc[df["temperature"] > 115, "quality_flag"] = "HIGH_TEMP"
    df.loc[df["pressure"] < 0, "quality_flag"] = "INVALID_PRESSURE"

    cleaned_count = len(df)

    # Save cleaned file
    output_file = "cleaned_" + file
    df.to_csv(os.path.join(PROCESSED_PATH, output_file), index=False)

    # Log quality metrics
    log = pd.DataFrame([{
        "file": file,
        "original_rows": original_count,
        "cleaned_rows": cleaned_count,
        "processed_time": datetime.now()
    }])

    if os.path.exists(LOG_PATH):
        log.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        log.to_csv(LOG_PATH, index=False)

    print(f"Processed {file}")


def run():
    files = os.listdir(RAW_PATH)

    for file in files:
        if file.endswith(".csv"):
            clean_file(file)

if __name__ == "__main__":
    run()
