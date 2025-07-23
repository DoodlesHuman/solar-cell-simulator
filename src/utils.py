import time
import logging
from functools import wraps

# Logging Set Up
logging.basicConfig(
    filename = "data/output/simulation.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"[TIMEIT] Function '{func.__name__}' ran in {duration:.6f}s")
        return  result
    return wrapper

def log_step(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        step_num = len(self.trajectory)  # number of completed steps
        logging.info(f"Step {step_num+1}: running {func.__name__} with {len(self.carriers)} carriers")
        return func(self, *args, **kwargs)
    return wrapper