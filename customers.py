import numpy as np
from .helpers_functions.positive_validator import require_positive


'''
Deteremining the number of customers n(t) at t < ti
a queue **D/D/1/(K-1)/FIFO** simulation if: inter-arrival pattern > service pattern

at 1/lambda <= t < ti: n(t) = floor(lambda * t) - floor((mue * t) - (mue/lambda))
'''
def dd1k_lam_gt(lam:np.double, mu:np.double, k:int, t:int):
    require_positive(lam,mu)
    
    if lam > mu:
        n_t = np.floor(t*lam) - np.floor((mu*t)-(mu/lam))
        return int(n_t)


'''
Deteremining the number of customers n(t) at t < ti
a queue **D/D/1/(K-1)/FIFO** simulation if: service pattern > inter-arrival pattern

at t < ti: n(t) = M + floor(lambda * t) - floor(mue * t)
'''
def dd1k_mu_gt(lam:np.double, mu:np.double, M:int, k:int, t:int):
    require_positive(lam,mu)
    
    if mu > lam:
        n_t = M + np.floor(t*lam) - np.floor(mu*t)
        return int(n_t)
    

'''
Deteremining the number of customers n(t) at any given time
a queue D/D/1/(K-1)/FIFO simulation if: service pattern = inter-arrival pattern

at t >=0: n(t) = M
'''    
def dd1k_mu_lam_equals(lam:np.double, mu:np.double, M:int, k:int, t:int):
    require_positive(lam,mu)

    if mu == lam:
        return M