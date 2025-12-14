import numpy as np
import math
from helpers.positive_validator import require_positive
from helpers.ti_calc import ti_calc

'''
Deteremining the waiting time Wq(n) for the n-th customer
for a queue **D/D/1/(K-1)/FIFO** 

if: inter-arrival pattern > service pattern (λ > μ)

at n == 0:           Wq(n) = 0
at n < floor(λ*t):   Wq(n) = (1/μ - 1/λ)(n-1)
at n >= floor(λ*t):  Wq(n) alternates between (1/μ - 1/λ)*(λ*ti - 2) and (1/μ - 1/λ)*(λ*ti - 3) 
'''

@require_positive
def dd1k_lam_gt(lam:np.double, mu:np.double, k:int, n:int):
   
    if lam > mu:

        if n == 0:
            return 0
        
        ti = ti_calc(lam, mu, 0, k)

        first_balked_customer = lam * ti
        term = (math.ceil(1/mu) - math.ceil(1/lam))

        if n < first_balked_customer:
            Wq = term * (n-1)
            return Wq
        
        #Special Case: if m(1/λ) == (1/μ)
        if math.ceil(1 / lam) % math.ceil(1 / mu) == 0:
            return term * (first_balked_customer - 2)


        if (n - int(first_balked_customer)) % 2 == 0:
            return term * (first_balked_customer - 2)
        return term * (first_balked_customer - 3)


'''
Deteremining the waiting time Wq(n) for the n-th customer
for a queue **D/D/1/(K-1)/FIFO** 

if: service pattern > inter-arrival pattern (μ > λ)

at n == 0:           Wq(n) = (M - 1) / (2 * mu)
at n < floor(λ*t):   Wq(n) = (M + n - 1) - n*(1/μ)
at n >= floor(λ*t):  Wq(n) = 0
'''

@require_positive
def dd1k_mu_gt(lam:np.double, mu:np.double, M:int, k:int, n:int):

    if n == 0:
        return (M - 1) / (2 * mu)
    
    ti = ti_calc(lam, mu, M, k)

    limit_customer = math.floor(lam * ti)
    if n <= limit_customer:
        return ( (M + n - 1) * math.ceil(1/mu) ) - ( n * math.ceil(1/lam) )

    return 0


'''
Deteremining the waiting time Wq(n) for the n-th customer
for a queue **D/D/1/(K-1)/FIFO** 

if: service pattern == inter-arrival pattern (μ == λ)
'''

@require_positive
def dd1k_mu_lam_equals(lam:np.double, mu:np.double, M:int, k:int, n:int):

    if mu == lam:
        return (M-1) * math.ceil(1/mu)