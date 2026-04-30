import random
import time

def getrandomtime(sd,ed):
    print(f"Printing random number between {sd} and {ed}")
    ranGenerator = random.random()

    dformat ="%d/%m/%Y"

    st = time.mktime(time.strptime(sd,dformat))
    et =time.mktime(time.strptime(ed,dformat))

    rant = st + ranGenerator * (et - st)

    rand = time.strftime(dformat,time.localtime(rant))

    return rand

print("Random date =",getrandomtime("1/1/2024" , "1/1/2028"))