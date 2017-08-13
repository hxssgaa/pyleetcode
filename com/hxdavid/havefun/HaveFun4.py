import threading
import time


def worker(worker_id, previous):
    """
    :type worker_id: int
    :type previous: threading.Thread
    """
    print(threading.currentThread().getName(), 'Starting')
    previous.join()
    print(threading.currentThread().getName(), 'Finished work')


previous = threading.main_thread()
for i in range(5):
    t = threading.Thread(target=worker, args=(i, previous))
    t.start()
    previous = t

time.sleep(1)
