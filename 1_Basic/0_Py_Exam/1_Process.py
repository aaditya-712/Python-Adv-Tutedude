from multiprocessing import Process 
import os

def task(): 
    print(f"Task executed by Process ID: {os.getpid()}") 
if __name__ == "__main__": 
    p1 = Process(target=task) 
    p2 = Process(target=task) 
    p1.start() 
    p2.start() 
    p1.join() 
    p2.join() 