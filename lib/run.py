import subprocess
import sys
from time import time

from lib.datestring import formatted_date_time

timeout = 60*10  # in seconds

def run(bin_args, file_name):
    path = sys.argv[0][0:-7]
    log_file_name = 'log_{}.csv'.format(formatted_date_time)
    log = open(path + log_file_name, "a")

    try:
        startTime = time()
        subprocess.run(args=[*bin_args, file_name], timeout=timeout, stdout=log)
        return time() - startTime
    except subprocess.TimeoutExpired:
        return timeout

    log.close()
