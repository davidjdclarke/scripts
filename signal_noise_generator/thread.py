# Part One
import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()

finish = time.perf_counter()

print('Finished in ' + str(finish-start) + ' seconds(s)')