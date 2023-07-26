from threading import Thread, Lock
from time import sleep
from random import random

def get_right(id: int, num_p: int) -> int:
    if id == num_p - 1:
        return 0
    else:
        return id + 1

def work(id: int, apetite: int, left_fork: Lock, right_fork: Lock):
    print(f"philosopher {id} working")

    for _ in range(apetite):
        print(f"Philosopher {id} is thinking")
        if id % 2 == 0:
            left_fork.acquire()
            right_fork.acquire()
        else:
            right_fork.acquire()
            left_fork.acquire()
        print(f"Philosopher {id} is eating")
        sleep(random())
        left_fork.release()
        right_fork.release()


if __name__ == "__main__":
    forks = [Lock() for _ in range(10)]
    threads: list[Thread] = []
    for i in range(10):
        # spawn 10 threads
        new_thread = Thread(target=work, args=[i, 10, forks[i], forks[get_right(i, 10)]])
        threads.append(new_thread)
        new_thread.start()

    for thread in threads:
        thread.join()

