#!/usr/bin/python
import commands
from Process import *
from Info import *

print ("PYGR04 - Help machines to control!\n")

processes = commands.getoutput("ps aux").split("\n")
del processes[0]

psaux = []

for process in processes:
    columns = " ".join(process.split()).split(" ")

    new = Process()
    new.user = columns[0]
    new.pid = columns[1]
    new.cpu = columns[2]
    new.mem = columns[3]
    new.vsz = columns[4]
    new.rss = columns[5]
    new.tty = columns[6]
    new.stat = columns[7]
    new.start = columns[8]
    new.time = columns[9]
    new.command = columns[10]

    psaux.append(new)

print ("There are %d active processes" % (len(psaux)))

users = []
infos = []
for process in psaux:
    if(process.user not in users):
        users.append(process.user)
        info = Info()
        info.user = process.user
        info.cpu = float(process.cpu)
        info.mem = float(process.mem)
        infos.append(info)
    else:
        for info in infos:
            if(info.user == process.user):
                info.number += 1
                info.cpu += float(process.cpu)
                info.mem += float(process.mem)
                break


print ("...and %d users using your memory.\n" % (len(users)))

print ("Which attribute you want to sort the list?")
print ("0 - By user")
print ("1 - By amount of processes")
print ("3 - By cpu use")
print ("4 - By memory use\n")

try:
    answer = int(input("Type here: "))

    while(answer < 0 or answer > 4):
        print("\nWrong choice, man. But at least you've entered a number... Try again!")
        answer = int(input("Type here: "))

    print ("Baah! I'll not order anyway.")

    print("\nUSER           AMOUNT          CPU             MEM")
    for info in infos:
        print("%s\t%s\t%s\t%s" % (
        info.user.ljust(10), str(info.number).rjust(5), str(info.cpu).rjust(10), str(info.mem).rjust(10)))
except:
    print("\nBad answer, bro!")