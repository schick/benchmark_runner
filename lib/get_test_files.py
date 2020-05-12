import sys
from os import listdir
from os.path import isfile, join

path_to_main = sys.argv[0][0:-7]
resources_path = path_to_main + "resources"

def get_test_files():
    return [resources_path + "/" + f for f in listdir(resources_path) if isfile(join(resources_path, f))]