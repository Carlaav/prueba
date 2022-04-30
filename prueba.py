from multiprocessing import Pool
import random
import time

def func(n):
    print("starting", n)
    duration = round(random.random(), 3)
    time.sleep(duration)
    print("finished", n, "time takem", duration, "seconds")
    return n, duration

urls = ["a.com", "b.com", "c.com", "d.com", "e.com", "f.com"]

if __name__ == "__main__":
    pool = Pool(processes=5)
    data = pool.map(func, urls)
