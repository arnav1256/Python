pnct = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,123,124,125]
import random
upper1 = chr(random.randint(65,90))
upper2 = chr(random.randint(65,90))
lower1 = chr(random.randint(97,122))
lower2 = chr(random.randint(97,122))
num1 = chr(random.randint(48,57))
num2 = chr(random.randint(48,57))
p1 = random.randint(0,len(pnct) - 1)
p2 = random.randint(0,len(pnct) - 1)
punct1 = chr(pnct[p1])
punct2 = chr(pnct[p2])
pswrd = [upper1, upper2, lower1, lower2, num1, num2, punct1, punct2]
pswrdd = random.shuffle(pswrd)
print(pswrd[0] + pswrd[1] + pswrd[2] + pswrd[3] + pswrd[4] + pswrd[5] + pswrd[6] + pswrd[7])
