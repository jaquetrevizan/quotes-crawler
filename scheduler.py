import schedule
import time
import subprocess
import sys

def job():
    python_path = sys.executable
    subprocess.run([python_path, "crawler.py"])

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
