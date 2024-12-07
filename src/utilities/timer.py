import timeit
from typing import Callable


def run_timed(f: Callable) -> None:
    timer = timeit.Timer(f)
    elapsed = timer.timeit(1)
    print(f'Time taken: {elapsed:.6f} seconds')
