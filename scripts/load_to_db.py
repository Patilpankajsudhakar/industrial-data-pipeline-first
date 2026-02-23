import pandas as pd
import os
from sqlalchemy import create_engine

PROCESSED_PATH = r"C:\Users\patil\OneDrive\Documents\Data Engineering\data-platform\processed"

# change password accordingly
engine = create_engine(
    "postgresql+psycopg2://postgres:Pune%40123@localhost:5432/data_platform"
)

def load_file(file):
    df = pd.read_csv(os.path.join(PROCESSED_PATH, file))

    df.rename(columns={"timestamp": "event_time"}, inplace=True)

    df.to_sql(
        "fact_machine_metrics",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {file}")

def run():
    for file in os.listdir(PROCESSED_PATH):
        if file.endswith(".csv"):
            load_file(file)

if __name__ == "__main__":
    run()