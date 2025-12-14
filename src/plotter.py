import matplotlib.pyplot as plt
import numpy as np
from src.customers import dd1k_lam_gt, dd1k_mu_gt, dd1k_mu_lam_equals
import matplotlib

matplotlib.use('Agg')

def generate_dd1_plot(lam, mu, M, K, output_file='simulation_result.png'):
    if lam > mu:
        max_time = int(K / (lam - mu)) + 15
    elif mu > lam:
        max_time = int(M / (mu - lam)) + 15 if M > 0 else 50
    else:
        max_time = 50
    
    if max_time > 60: max_time = 60

    t_values = np.arange(0, max_time + 1, 1)
    n_values = []
    for t in t_values:
        if lam > mu:
            val = dd1k_lam_gt(lam, mu, K, t)
        elif mu > lam:
            val = dd1k_mu_gt(lam, mu, M, K, t)
        else:
            val = dd1k_mu_lam_equals(lam, mu, M, K, t)
        n_values.append(val)

    arrivals = []
    services = []
    departures = []

    arrival_interval = 1/lam if lam > 0 else 999
    service_time = 1/mu if mu > 0 else 999
    next_free_server_time = 0.0
    
    for i in range(M):
        label = f"M{i+1}"
        start_t = next_free_server_time
        services.append((start_t, label))
        end_t = start_t + service_time
        departures.append((end_t, label))
        next_free_server_time = end_t

    num_new_customers = int(max_time * lam)
    for i in range(num_new_customers):
        label = f"C{i+1}"
        arr_t = (i + 1) * arrival_interval
        if arr_t > max_time: break
        arrivals.append((arr_t, label))
        start_t = max(arr_t, next_free_server_time)
        if start_t <= max_time:
            services.append((start_t, label))
            end_t = start_t + service_time
            if end_t <= max_time:
                departures.append((end_t, label))
            next_free_server_time = end_t

    fig, ax = plt.subplots(figsize=(16, 10))
    max_n_graph = max(n_values) if n_values else 5
    base_h = max_n_graph + 1
    line_depart = base_h + 2
    line_service = base_h + 5
    line_arrival = base_h + 8
    top_limit = line_arrival + 2

    ax.hlines(y=[line_arrival, line_service, line_depart], xmin=0, xmax=max_time, colors='black', linewidth=1)
    ax.text(0, line_arrival + 0.5, "A customer arrives", fontweight='bold', fontsize=12)
    ax.text(0, line_service + 0.5, "A customer enters to be served", fontweight='bold', fontsize=12)
    ax.text(0, line_depart + 0.5, "Departures", fontweight='bold', fontsize=12)

    for t in range(0, int(max_time) + 1, 2):
        ax.axvline(x=t, color='gray', linestyle='--', alpha=0.3)

    for t, lbl in arrivals:
        ax.annotate('', xy=(t, line_arrival), xytext=(t, line_arrival + 1.5),
                    arrowprops=dict(facecolor='#4169E1', width=2, headwidth=8))
        ax.text(t, line_arrival - 0.8, lbl, ha='center', va='top', fontsize=9, fontweight='bold')
        ax.plot([t, t], [line_arrival, line_service], color='gray', linestyle=':', alpha=0.5)

    for t, lbl in services:
        color = 'black' if 'M' in lbl else '#4169E1'
        ax.annotate('', xy=(t, line_service), xytext=(t, line_service + 1.5),
                    arrowprops=dict(facecolor=color, width=2, headwidth=8))
        if 'M' in lbl:
             ax.text(t, line_service + 1.6, lbl, ha='center', fontsize=9)

    for t, lbl in departures:
        ax.annotate('', xy=(t, line_depart - 1.5), xytext=(t, line_depart),
                    arrowprops=dict(facecolor='#D2691E', width=2, headwidth=8))

    ax.step(t_values, n_values, where='post', color='#8B0000', linewidth=3, label='n(t)')
    ax.text(0.5, n_values[0] + 0.5, "n(t)", fontsize=14, fontweight='bold')

    ax.set_xlim(0, max_time)
    ax.set_ylim(0, top_limit)
    
    ax.set_xticks(np.arange(0, max_time + 1, 2))
    
    ax.set_yticks(np.arange(0, max_n_graph + 2, 1))
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    return output_file