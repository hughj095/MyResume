import time

class Timer:
    def timer(self, minutes):
        seconds = minutes * 60
        print('started timer')
        while seconds:
            mins, secs = divmod(seconds, 60)
            time.sleep(1)
            seconds -= 1