import csv
from datetime import datetime

LOG_FILE = "detections.csv"

def log_detection(user_id, confidence):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), user_id, confidence])
