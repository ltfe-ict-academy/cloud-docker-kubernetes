import time
from datetime import datetime

if __name__ == "__main__":
    print("Strating proccesing app!!")
    while True:
        time.sleep(1)  # simulate work
        timestamp = datetime.now()
        print(f"[{timestamp}] Working!")
