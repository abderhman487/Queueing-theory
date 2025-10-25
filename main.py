import numpy as np
import matplotlib.pyplot as plt

lam = eval(input("Enter the inter-arrival rate λ: "))
mu = eval(input("Enter the service-time rate μ: "))
time = eval(input("The requested time t: "))

#function for D/D/1/(K-1)/FIFO simulation if inter-arrival > service
def dd1k(lam,mu,t):
    if lam <= 0 or mu <= 0:
        raise ValueError("λ and μ must be positive numbers.")
    
    if lam > mu:
        n_t = np.floor(t*lam) - np.floor((mu*t)-(mu/lam))
        return int(n_t)

result = dd1k(lam,mu,time)

print(f"n(t) = {result}")
