#!/home/sulantha/anaconda3/bin/python
import random
import sys
import numpy as np
from sklearn.cross_validation import StratifiedShuffleSplit
import copy

totalargs = len(sys.argv)
cmdargs = str(sys.argv)
if totalargs == 5:
    print('Need exactly 6 arguments. <Main CSV> <r - sampling portion> <strat col number> <number of simulations> <output folder>')
    print('Sample map will be in the first column and the your sampled value be 2')
    sys.exit(0)

CSV = sys.argv[1]
r = float(sys.argv[2])
stratCol = int(float(sys.argv[3]))
ns = int(float(sys.argv[4]))
of = sys.argv[5]

CSV = [s.split(',') for s in open(CSV, 'r').readlines()]
Header = CSV[0]
Header.insert(0, 'SAMPLE')
CSV.pop(0)
Y = np.array([line[stratCol - 1] for line in CSV])
X = np.array([i for i in range(len(CSV))])
SSS = StratifiedShuffleSplit(Y, ns, test_size=r, random_state=0)
count = 1
CSV_RESET = copy.deepcopy(CSV)
for train_index, test_index in SSS:
    CSV = copy.deepcopy(CSV_RESET)
    X_train, X_test = X[train_index], X[test_index]
    [CSV[i].insert(0, '1') for i in X_train]
    [CSV[i].insert(0, '2') for i in X_test]
    opList = [','.join(Header)]
    fCSV = []
    for l in CSV:
        l_ = ','.join(l)
        opList.append(l_)

    opFname = '{0}/SET_{1}.csv'.format(of, count)
    opF = open(opFname, 'w')
    for item in opList:
        opF.write("%s" % item)
    opF.close()
    count +=1
