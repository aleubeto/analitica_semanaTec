arr = []
flag = True
for i in open("insurance.csv", "rt"):
    if flag:
        flag=False
        continue
    arr.append(int(i.split(",")[0]))
sum(arr)/len(arr)