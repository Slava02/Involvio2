import schedule
import time

def hello_world():
    print("Hello, World!")

schedule.every().thursday.at("11:49", "Europe/Moscow").do(hello_world)

while True:
    schedule.run_pending()
    time.sleep(1)