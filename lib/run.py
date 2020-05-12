import subprocess
from time import time

timeout = 60*10  # in seconds

def run(bin_args, file_name):
    try:
        startTime = time()
        subprocess.run(args=[*bin_args, file_name], timeout=timeout)
        return time() - startTime
    except subprocess.TimeoutExpired:
        return timeout
