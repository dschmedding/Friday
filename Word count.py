fp = open("/Users/dschmedding/PycharmProjects/Friday/Dracula", "r")
fp2 = open("/Users/dschmedding/PycharmProjects/Friday/Harry Potter", "w")
list = []
fp_contents = fp.read()
punct = "/°^!£$%&()=?^*+§°ç><,;:.-_{}"
line = " "
for p in fp_contents:
     if p not in punct:
        line = line + p
line = line.split()

for x in line:
    if x not in list:
        list.append(x)
        fp2.write(str(x) + "\n")

print(len(list))