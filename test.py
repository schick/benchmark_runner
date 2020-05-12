import subprocess

call = "gedit"
args = "/home/maxi/Code/Runner/resources/satcoin-genesis-SAT-512.cnf"

try:
    subprocess.run(args=[call, args], timeout=1)
except subprocess.TimeoutExpired:
    print("Timeout")