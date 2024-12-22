import time 

def stopwatch():
    i = input(":")
    if i.lower() == "start":
        start_time = time.time()
    
    while True:
        u = input(":")
        if u.lower() == "stop":
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{elapsed_time:.2f}")
            break
stopwatch()