import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Pune%40123@localhost:5432/data_platform"
)

def run_checks():

    query = """
    SELECT
        COUNT(*) AS total_rows,
        AVG(temperature) AS avg_temp,
        SUM(CASE WHEN quality_flag != 'GOOD' THEN 1 ELSE 0 END) AS bad_records
    FROM fact_machine_metrics;
    """

    df = pd.read_sql(query, engine)

    total = df["total_rows"][0]
    avg_temp = df["avg_temp"][0]
    bad = df["bad_records"][0]

    print("\n--- DATA HEALTH REPORT ---")
    print("Total Rows:", total)
    print("Average Temperature:", round(avg_temp,2))
    print("Bad Records:", bad)

    # Simple alert rules
    if bad > 10:
        print("⚠️ ALERT: Too many bad records!")

    if avg_temp > 110:
        print("⚠️ ALERT: Abnormal temperature trend!")

if __name__ == "__main__":
    run_checks()