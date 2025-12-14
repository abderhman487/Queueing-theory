import math
from src.customers import dd1k_lam_gt, dd1k_mu_gt, dd1k_mu_lam_equals
from src.waiting import dd1k_lam_gt as wq_lam_gt, dd1k_mu_gt as wq_mu_gt
from helpers.ti_calc import ti_calc

def test_lam_gt():
    # Case 1: Lambda > Mu (Lecture 4 - Example 1)
    # λ = 1/3, μ = 1/5, K = 4 (Assumed small K for testing)
    print("\n[Test 1] D/D/1/K-1 where λ > μ")
    lam, mu, M, K = 1/3, 1/5, 0, 4
    
    print(f"Inputs: λ={lam:.2f}, μ={mu:.2f}, K={K}")
    
    ti = ti_calc(lam, mu, M, K)
    print(f"Saturation Time (ti): {ti}")
    
    # Check n(t) at t=15 (Example)
    nt = dd1k_lam_gt(lam, mu, K, 15)
    print(f"n(15): {nt}")
    
    # Check Wq(n) for customer 2
    wq = wq_lam_gt(lam, mu, K, 2)
    print(f"Wq(2): {wq}")

def test_mu_gt():
    # Case 2: Mu > Lambda (Lecture 2 - Slide 25)
    # λ = 1/3, μ = 1, M = 7, K = 5
    print("\n[Test 2] D/D/1/K-1 where μ > λ")
    lam, mu, M, K = 1/3, 1.0, 7, 5

    print(f"Inputs: λ={lam:.2f}, μ={mu}, M={M}, K={K}")

    ti = ti_calc(lam, mu, M, K)
    print(f"Empty Time (ti): {ti}")
    assert ti == 10, f"Error: Expected ti=10 but got {ti}"

    # Check n(t) at t=0 and t=3
    print(f"n(0): {dd1k_mu_gt(lam, mu, M, K, 0)}")
    print(f"n(3): {dd1k_mu_gt(lam, mu, M, K, 3)}")

    # Check Wq(n) for customer 0 (Initial)
    wq_0 = wq_mu_gt(lam, mu, M, K, 0)
    print(f"Wq(0): {wq_0}") 
    
    # Check Wq(n) for customer 3
    wq_3 = wq_mu_gt(lam, mu, M, K, 3)
    print(f"Wq(3): {wq_3}")

def test_equal():
    # Case 3: Lambda == Mu
    print("\n[Test 3] D/D/1/K-1 where λ == μ")
    lam, mu, M, K = 0.5, 0.5, 5, 10
    
    print(f"Inputs: λ={lam}, μ={mu}, M={M}")
    
    nt = dd1k_mu_lam_equals(lam, mu, M, K, 10)
    print(f"n(10): {nt}")
    assert nt == M, "Error: n(t) should remain constant/oscillate near M"

if __name__ == "__main__":
    test_lam_gt()
    test_mu_gt()
    test_equal()