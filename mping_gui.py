from tkinter import *
from ping3 import ping
import time



def my_ping():

    res = [[ip, ping(ip, timeout=0.1, size=128)] for ip in ips]
    resp = time.strftime("%H:%M:%S\n\n")
    for ip, rtt in res:
        resp += ip + " "*(50-len(ip))
        if rtt is None:
            resp += "\tFAIL" + '\n'
        else:
            resp += "\tOK" + '\n'
    my_label.config(text=resp)
    my_label.after(1000, my_ping)

with open("ip.txt",'r') as fin:
    ips = fin.read().splitlines()


root = Tk()
root.title("pinger")
geo = "400x"+str(len(ips*19)+50)
root.geometry(geo)

my_label = Label(root, text="", justify=LEFT, font=('CourierNew'))
my_label.pack()


my_ping()

root.mainloop()
