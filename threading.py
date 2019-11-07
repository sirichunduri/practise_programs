import logging
import threading
import time
import concurrent.futures

def thread_function():
    time.sleep(0)

if __name__ == "__main__":

    threads = list()
    for index in range(3):
        #logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function)
        #print(threading.enumerate())
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        #print(index,thread)
        thread.join()


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function,range(3))