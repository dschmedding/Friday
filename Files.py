fp = open("my_text.text", "r")
fp2 = open("reult.txt", "w")

for each_line in fp:
    fp2.write(each_line[0:-1] + "Bob \n")

fp.close()
fp2.close()

