from helpers.positive_validator import require_positive


"""
Function to calculate M/M/1 metrics.

If k is provided, it uses Finite Capacity formulas.

If k is None, it uses Infinite Capacity formulas.
"""

@require_positive
def calc_mm1_metrics(lam, mu, k=None):
    rho = lam / mu  # Traffic intensity

    # M/M/1/infinity
    if k is None:
        if lam >= mu:
            raise ValueError("System is unstable (λ must be < μ for Infinite M/M/1).")
        
        P0 = 1 - rho
        L = rho / (1 - rho)
        Lq = (rho ** 2) / (1 - rho)
        W = 1 / (mu - lam)
        Wq = rho / (mu - lam)
        
        return {
            "model": "M/M/1/∞",
            "rho": rho,
            "P0": P0,
            "L": L, "Lq": Lq, "W": W, "Wq": Wq
        }

    # M/M/1/K
    else:
        # K includes the customer in service (System Size)
        k = int(k)
        
        # 1. Calculate P0 (Probability of empty system)
        if rho == 1.0:
            P0 = 1 / (k + 1)
        else:
            P0 = (1 - rho) / (1 - (rho ** (k + 1)))

        # 2. Calculate Pk (Probability system is full -> Lost Customers)
        if rho == 1.0:
            Pk = 1 / (k + 1)
        else:
            Pk = P0 * (rho ** k)
        
        # 3. Effective Lambda (Lambda that actually enters the system)
        lam_eff = lam * (1 - Pk)

        # 4. Calculate L (Avg customers in system)
        if rho == 1.0:
            L = k / 2
        else:
            # Standard formula for finite queue L
            numerator = 1 - ((k + 1) * (rho ** k)) + (k * (rho ** (k + 1)))
            denominator = (1 - rho) * (1 - (rho ** (k + 1)))
            L = rho * (numerator / denominator)

        # 5. Calculate other metrics using Little's Law with Lambda Effective
        W = L / lam_eff 
        Wq = W - (1 / mu)
        Lq = lam_eff * Wq

        return {
            "model": f"M/M/1/{k}",
            "rho": rho,
            "P0": P0,
            "Pk": Pk,
            "lambda_eff": lam_eff,
            "L": L, "Lq": Lq, "W": W, "Wq": Wq
        }


"""Calculates Probability of exactly n customers: P(n)"""

def calculate_pn(lam, mu, n, k=None):
    rho = lam / mu
    
    # Get P0 from the main calculator logic
    metrics = calc_mm1_metrics(lam, mu, k)
    P0 = metrics["P0"]

    if k is not None and n > k:
        return 0.0
    
    return P0 * (rho ** n)