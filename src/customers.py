import numpy as np
import math
from helpers.positive_validator import require_positive
from helpers.ti_calc import ti_calc


'''
Deteremining the number of customers n(t) at t < ti
a queue **D/D/1/(K-1)/FIFO** simulation

if: inter-arrival pattern > service pattern (λ > μ)

at t < 1/λ:         n(t) = 0
at 1/λ <= t < ti:   n(t) = floor(λ * t) - floor((μ * t) - (μ/λ))
at t >= ti:         n(t) alternates between k-1, k-2
'''

@require_positive
def dd1k_lam_gt(lam:np.double, mu:np.double, k:int, t:int):

    if lam > mu:
        ti = ti_calc(lam, mu, 0, k)

        const_arrival_time = math.ceil(1 / lam)
        const_service_time = math.ceil(1 / mu)

        if t < const_arrival_time:
            return 0

        if t >= const_arrival_time and t < ti:
            n_t = math.floor(t*lam) - math.floor((mu*t)-(mu/lam))
            return int(n_t)

        #Special Case: if m(1/λ) == (1/μ)
        if const_arrival_time % const_service_time == 0:
            return k
        
        time_since_last_arrival = t % const_arrival_time

        if time_since_last_arrival < const_service_time:
            return k - 1
        return k - 2



'''
Deteremining the number of customers n(t) at any given time
a queue **D/D/1/(K-1)/FIFO** simulation

if: service pattern > inter-arrival pattern (μ > λ)

at t < ti:  n(t) = M + floor(λ * t) - floor(μ * t)
at t >= ti: n(t) alternates between 0 and 1
'''

@require_positive
def dd1k_mu_gt(lam:np.double, mu:np.double, M:int, k:int, t:int):
    
    if mu > lam:
        ti = ti_calc(lam, mu, M, k)
        
        if t < ti:
            n_t = M + math.floor(t*lam) - math.floor(mu*t)
            return int(n_t)

        last_arrival_time = math.floor(t * lam) / lam
        departure_time = last_arrival_time + math.ceil(1 / mu)

        if t < departure_time:
                return 1
        else:
                return 0


'''
Deteremining the number of customers n(t) at any given time
a queue D/D/1/(K-1)/FIFO simulation

if: service pattern == inter-arrival pattern (μ == λ)

at t >=0: n(t) = M
'''

@require_positive
def dd1k_mu_lam_equals(lam:np.double, mu:np.double, M:int, k:int, t:int):

    if mu == lam:
        return M