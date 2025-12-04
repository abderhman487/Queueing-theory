from src import customers
from src import waiting

#User Inputs
choice = int(input("""Enter your requested system:
                   1- D/D/1/k-1
                   2- M/M/1/∞

                   Warning: your choice must be 1 or 2: """))

if choice != 1 and choice != 2:
    raise ValueError("Enter a valid choice (1 or 2).")

if choice == 1:
        
        lam = eval(input("Enter the inter-arrival rate into the system (λ): "))
        if lam <= 0:
            raise ValueError("λ and μ must be positive numbers.")

        mu = eval(input("Enter the service-time rate at the system (μ): "))
        if mu <=0:
            raise ValueError("λ and μ must be positive numbers.")

        if mu >= lam:
            M = int(input("Enter the initial customers in the system (M): "))

        k = int(input("Enter the limit on the system size (k-1): "))

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
                n_input = input("Enter the requested time t (or enter 'q' to exit): ")

                if n_input.lower() == 'q':
                    break

                n = eval(n)
                if lam > mu:
                    wq_val = waiting.dd1k_lam_gt(lam, mu, k, n)
                elif mu > lam:
                    wq_val = waiting.dd1k_mu_gt(lam, mu, M, k, n)
                elif mu == lam:
                    wq_val = waiting.dd1k_mu_lam_equals(lam, mu, M, k, n)

                print(f"Wq({n}) = {wq_val}")