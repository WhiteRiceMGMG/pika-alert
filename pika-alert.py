import time
from datetime import datetime, timedelta
import locale
import network, requests

token = 'your notify token'

def send_message(message):
    line_header  = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer' + ' ' + token }
    line_message = 'message=' + message 
    print(line_message)
    req = requests.post('https://notify-api.line.me/api/notify', headers = line_header, data = line_message)
    req.close()
    
def wait_time(ExeHour, ExeMinute, ExeSecond):
    now = datetime.now()
    print(now)
    next_exe = now.replace(hour=ExeHour, minute=ExeMinute, second=ExeSecond, microsecond=0)

    if next_exe <= now:
        next_exe += timedelta(days=1)

    wait_time_seconds = (next_exe - now).total_seconds()
    print(wait_time_seconds)
    time.sleep(wait_time_seconds)

    if next_exe <= now:
        next_exe += timedelta(days=1)

def task1():
    message = "TIMEZORN:UTC"
    send_message(message)
wait_time(13,0,0)
task1()


