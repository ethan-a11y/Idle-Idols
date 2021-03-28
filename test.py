import threading

def gfg():
    print("GeeksforGeeks\n")

timer = threading.Timer(2.0, gfg)
timer.start()