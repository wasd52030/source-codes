import time
from datetime import timedelta


def FuncTimer(func):
    def wrap():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f"執行共花 {timedelta(seconds=t2-t1)}")

    return wrap
