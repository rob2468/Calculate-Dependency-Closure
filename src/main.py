#!/usr/bin/env python

from data import DNUM

import random
import time

def CalculateDepClosure(Dep):
    reachable = []
    for i in range(DNUM):
        row = []
        for j in range(DNUM):
            row.append(-1)
        reachable.append(row)
    for i in range(DNUM):
        for j in range(DNUM):
            if random.randint(0, 9) == 0:
                reachable[i][j] = 1
    for k in range(DNUM):
        for i in range(DNUM):
            for j in range(DNUM):
                if reachable[i][j]==-1 and reachable[i][k]!=-1 and reachable[k][j]!=-1:
                    reachable[i][j]=1
                    
    for i in range(DNUM):
        for j in range(DNUM):
            if reachable[i][j]!=-1:
                Dep.append((i, j))
    
if __name__=="__main__":
    starttime=time.time()
    Dep = []
    CalculateDepClosure(Dep)
    endtime=time.time()
    print (endtime-starttime), "ms"
    
