import subprocess
from datetime import datetime

def run_step(name, command):
    print(f"\nStarting: {name}")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"FAILED: {name}")
        exit()
    else:
        print(f"Completed: {name}")

print("Pipeline Started at", datetime.now())

run_step("Data Generation", "python data_generator.py")
run_step("Data Cleaning", "python data_cleaner.py")
run_step("Load to Database", "python load_to_db.py")
run_step("Data Monitoring", "python data_monitor.py")

print("Pipeline Finished Successfully")