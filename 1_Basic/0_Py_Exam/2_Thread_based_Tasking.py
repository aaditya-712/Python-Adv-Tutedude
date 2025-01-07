from threading import Thread, current_thread 

def task(): 
    print(f"Task executed by Thread: {current_thread().name}\n") 

t1 = Thread(target=task, name='Thread-1') 
t2 = Thread(target=task, name='Thread-2') 
t1.start() 
t2.start() 
t1.join() 
t2.join()