from src import customers
from src import waiting
from src import stochastic_customers
from src import plotter

#User Inputs
choice = int(input("""Enter your requested system:
                   1- D/D/1/k-1
                   2- M/M/1/∞

                   Warning: your choice must be 1 or 2: """))

if choice != 1 and choice != 2:
    raise ValueError("Enter a valid choice (1 or 2).")

if choice == 1:
    print("\n--- D/D/1 Deterministic System ---")
    lam = eval(input("Enter the inter-arrival rate into the system (λ): "))
    if lam <= 0:
        raise ValueError("λ and μ must be positive numbers.")

    mu = eval(input("Enter the service-time rate at the system (μ): "))
    if mu <=0:
        raise ValueError("λ and μ must be positive numbers.")

    M = 0
    if mu >= lam:
        M = int(input("Enter the initial customers in the system (M): "))

    k = int(input("Enter the limit on the system size (k-1): "))

    want_plot = input("\nGenerate Simulation Plot? (y/n): ")
    if want_plot.lower() == 'y':
        output_img = plotter.generate_dd1_plot(lam, mu, M, k)
        print(f"Plot saved to '{output_img}'")

    while True:
        n_t = 0
        t_input = input("Enter the requested time t (or enter 'q' to exit): ")

        if t_input.lower() == 'q':
            break

        t = eval(t_input)

        if lam > mu:
            n_t = customers.dd1k_lam_gt(lam, mu, k, t)

        if mu > lam:
            n_t = customers.dd1k_mu_gt(lam, mu, M, k, t)    

        if mu == lam:
            n_t = customers.dd1k_mu_lam_equals(lam, mu, M, k, t)

        print(f"n(t)= {n_t}")

    calc_wq = input("Do you want to calculate Waiting Time Wq(n)? (y/n): ")
    if calc_wq.lower() == 'y':
        while True:
            wq_val = 0
            n_input = input("Enter the requested customer number n (or enter 'q' to exit): ")

            if n_input.lower() == 'q':
                break

            n = int(n_input)
            if lam > mu:
                wq_val = waiting.dd1k_lam_gt(lam, mu, k, n)
            elif mu > lam:
                wq_val = waiting.dd1k_mu_gt(lam, mu, M, k, n)
            elif mu == lam:
                wq_val = waiting.dd1k_mu_lam_equals(lam, mu, M, k, n)

            print(f"Wq({n}) = {wq_val}")


if choice == 2:
    print("\n--- M/M/1 Stochastic System ---")
    lam = float(input("Enter the inter-arrival rate into the system (λ): "))
    mu = float(input("Enter the service-time rate at the system (μ): "))
    
    is_finite = input("Is there a system capacity limit (K)? (y/n): ")
    
    k_val = None
    if is_finite.lower() == 'y':
        k_val = int(input("Enter the system capacity K (Queue + Server): "))

    try:
        metrics = stochastic_customers.calc_mm1_metrics(lam, mu, k_val)
        
        print(f"\n--- Results for {metrics['model']} ---")
        print(f"Traffic Intensity (ρ)  : {metrics['rho']:.4f}")
        print(f"Prob. of Empty (P0)    : {metrics['P0']:.4f}")
          
        if k_val:
            print(f"Prob. of Full (Pk)     : {metrics['Pk']:.4f} (Lost Customers)")
            print(f"Effective λ (λ_eff)    : {metrics['lambda_eff']:.4f}")
            
        print("-" * 30)
        print(f"Avg Customers in System (L) : {metrics['L']:.4f}")
        print(f"Avg Customers in Queue (Lq) : {metrics['Lq']:.4f}")
        print(f"Avg Time in System (W)      : {metrics['W']:.4f}")
        print(f"Avg Time in Queue (Wq)      : {metrics['Wq']:.4f}")

        # Optional P(n)
        check_prob = input("\nCalculate probability P(n)? (y/n): ")
        if check_prob.lower() == 'y':
            n_val = int(input("Enter n: "))
            pn = stochastic_customers.calculate_pn(lam, mu, n_val, k_val)
            print(f"P({n_val}) = {pn:.4f}")

    except ValueError as e:
        print(f"Error: {e}")