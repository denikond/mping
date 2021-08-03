from os import system, name
from ping3 import ping
import time


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


with open("ip.txt",'r') as fin:
    ips = fin.read().splitlines()


while True:

    res = [[ip, ping(ip, timeout=0.1, size=128)] for ip in ips]
    resp = time.strftime("%H:%M:%S\n\n")
    for ip, rtt in res:
        resp += ip + " "*(50-len(ip))
        if rtt is None:
            resp += "\tFAIL" + '\n'
        else:
            resp += "\tOK" + '\n'
    clear()
    print(resp)
    time.sleep(1)
