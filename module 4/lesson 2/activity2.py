def pm(t):
    rev =len(t)-1
    front =0
    while (front<rev):
        if (t[front] != t[rev]):
            return False
        front += 1
        rev -= 1

    return True

t =(1,2,3,3,2,1)
if (pm(t)):
    print("The tuple is flip-flop")

else:
    print("Not flip-flop")