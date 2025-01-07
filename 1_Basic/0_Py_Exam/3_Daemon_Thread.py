from threading import Thread 
import time 
def background_task(): 
    while True: 
        print("Running background task...") 
        time.sleep(1) 
        
t = Thread(target=background_task, daemon=True) 
t.start() 
time.sleep(3) 
print("Main program ends") 
