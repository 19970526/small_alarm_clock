import datetime
from multiprocessing import Process
import time
import winsound


def stop(interval):
    start_time = time.time()
    time.sleep(int(interval))
    end_time = time.time()
    return end_time - start_time
    

def ring(set_time):
    while True:
        # 实际时间
        ring_time = datetime.datetime.now().strftime('%H:%M')
        
        # 如果时间到就响铃
        if ring_time == set_time:
            winsound.PlaySound(r'..\matter\music.wav', winsound.SND_NODEFAULT)

        
if __name__ == '__main__':
    # 设置闹钟时间
    set_time = input("何时响铃(00:00格式)：")
    interval = input("响铃时间(秒)：")
    
    stop_process = Process(target = stop, args = (interval, ))
    ring_process = Process(target = ring, args = (set_time, ))
    
    stop_process.start()
    ring_process.start()
    
    stop_process.join()
    ring_process.terminate()
    