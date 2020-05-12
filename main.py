import sys
from datetime import datetime

from lib.get_test_files import get_test_files
from lib.run import run

path = sys.argv[0][0:-7]
formatted_date_time = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
out_file_name = 'output_{}.csv'.format(formatted_date_time)
file = open(path + out_file_name, "x")

bin_args = sys.argv[1:]
file.write(str(bin_args) + "\n")

test_files = get_test_files()

for file_name in test_files:
    elapsed_time = run(bin_args, file_name)

    file.write("{},{}\n".format(file_name, elapsed_time))

file.close()




