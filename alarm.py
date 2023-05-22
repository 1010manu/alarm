
import time
def alarm(seconds):
    time_pass=0
    while time_pass<seconds:
        time.sleep(1)
        time_pass+=1
        time_left=seconds-time_pass
        minutes_left=time_left//60
        seconds_left=time_left%60
        print(f"{minutes_left:02}:{seconds_left:02}")
    print('time to wake up')
minutes=int(input('how many minutes:'))
seconds=int(input('how many seconds:'))
total_seconds=minutes*60+seconds
alarm(total_seconds)

        
