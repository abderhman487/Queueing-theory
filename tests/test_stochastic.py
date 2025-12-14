from src.stochastic_customers import calc_mm1_metrics

def test_mm1_infinite():
    # Case 1: Infinite Capacity (Lecture 5 - Example 1)
    print("\n[Test 1] M/M/1/∞ (Infinite)")
    # λ = 50 jobs/hr, μ = 60 jobs/hr
    lam, mu = 50.0, 60.0
    
    print(f"Inputs: λ={lam}, μ={mu}")
    
    res = calc_mm1_metrics(lam, mu, k=None)
    
    print(f"L  (Expected 5.0): {res['L']:.2f}")
    print(f"W  (Expected 0.1): {res['W']:.2f}")
    print(f"Wq (Expected 0.083): {res['Wq']:.4f}")
    
    assert abs(res['L'] - 5.0) < 1e-5, "L calculation wrong"

def test_mm1_finite():
    # Case 2: Finite Capacity (M/M/1/K)
    print("\n[Test 2] M/M/1/K (Finite)")
    # λ = 3, μ = 4, K = 3 (Queue+Server)
    lam, mu, K = 3.0, 4.0, 3
    
    print(f"Inputs: λ={lam}, μ={mu}, K={K}")
    
    res = calc_mm1_metrics(lam, mu, k=K)
    
    print(f"P0 (Empty Prob): {res['P0']:.4f}")
    print(f"Pk (Loss Prob): {res['Pk']:.4f}")
    print(f"L  (Avg System): {res['L']:.4f}")
    print(f"Effective λ: {res['lambda_eff']:.4f}")

if __name__ == "__main__":
    test_mm1_infinite()
    test_mm1_finite()