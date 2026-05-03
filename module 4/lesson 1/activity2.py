def mw(words):
    ctr =0
    l =[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr = ctr + 1
            l.append(word)

    return ctr

c = print(mw(["aba","ba","ifi","010101","mm"]))
print("Number of words having the first and last letter same",c)