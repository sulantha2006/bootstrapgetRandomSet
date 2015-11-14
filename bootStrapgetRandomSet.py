
import random
import sys

totalargs = len(sys.argv)
cmdargs = str(sys.argv)
if totalargs == 5:
    print('Need exactly 4 arguments. <Main CSV> <n - total subs> <r - sampling size> <number of simulations> <output folder>')
    sys.exit(0)

CSV = sys.argv[1]
n = int(float(sys.argv[2]))
r = int(float(sys.argv[3]))
ns = int(float(sys.argv[4]))
of = sys.argv[5]

CSV = open(CSV, 'r').readlines()

for sim in range(ns):
    randset = random.sample(range(0, n-1), r)
    opList = [CSV[i] for i in randset]
    opFname = '{0}/{1}.csv'.format(of, sim)
    opF = open(opFname, 'w')
    for item in opList:
        opF.write("%s" % item)
    opF.close()