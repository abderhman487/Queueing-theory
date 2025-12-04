import numpy as np
import math

'''
Deteremining the ti (the smallest real number that satisfying the used equation)
for a queue D/D/1/(K-1)/FIFO
'''
def ti_calc(lam:np.double, mu:np.double, M:int, k:int):

    if lam > mu:
        # ti is when n(t) == k+1 because k is the max value rhe queue can handle
        k_max = k+1

        approximate_ti = (k_max-(mu/lam)) / (lam-mu)
        t_start = int(max(1, approximate_ti - 10)) #max(1,ti) because ti - 10 could be negative
        t_end = int(approximate_ti + 20)

        for t in range(t_start,t_end):
            n_t = math.floor(t*lam) - math.floor((mu*t)-(mu/lam))
            if n_t == k_max:
                return t
            
    if mu > lam:
        # ti is when n(t) == 0

        approximate_ti = M / (mu - lam)
        t_start = int(max(1, approximate_ti - 10))
        t_end = int(approximate_ti + 20)

        for t in range(t_start,t_end):
            n_t = M + math.floor(t*lam) - math.floor(mu*t)
            if n_t == 0:
                return t
            
    if mu == lam:
        # ti = M
        return 0 