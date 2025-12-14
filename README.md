# Queueing Theory Simulator

A Python-based simulator for analyzing Deterministic (D/D/1) and Stochastic (M/M/1) queueing systems. This tool calculates performance metrics such as the number of customers in the system $n(t)$, waiting times $W_q(n)$, and steady-state probabilities based on user inputs.

## Features

* **Deterministic Models (D/D/1/K-1):**
    * Handles cases where $\lambda > \mu$, $\mu > \lambda$, and $\lambda = \mu$.
    * Calculates number of customers $n(t)$ at any specific time $t$.
    * Calculates Waiting Time in Queue $W_q(n)$ for the $n$-th customer.
    * Supports finite system capacity ($K$) and initial customers ($M$).

* **Stochastic Models (M/M/1):**
    * Supports Infinite Capacity ($M/M/1/\infty$).
    * Supports Finite Capacity ($M/M/1/K$).
    * Calculates Steady-State Performance Measures: $L$, $L_q$, $W$, $W_q$.
    * Calculates probabilities: $P_0$ (empty system), $P_k$ (full system), and $P_n$ (probability of $n$ customers).

## Prerequisites

Ensure **Python 3.x** is installed on your system.

## Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/abderhman487/Queueing-theory.git
    cd Queueing-theory
    ```

2.  **Create and Activate Virtual Environment:**
    * *Linux / macOS:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * *Windows:*
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the simulator, run the main script:

```bash
python main.py
````

Follow the on-screen prompts to:

1.  Choose the system type (`1` for D/D/1 or `2` for M/M/1).
2.  Enter the required rates ($\lambda$, $\mu$) and system parameters ($M$, $K$).
3.  Query for specific calculations (e.g., $n(t)$ at a specific time or $W_q$ for a specific customer).

## Running Tests

The project includes unit tests to verify calculations against known examples from lectures.

**To run the Deterministic tests:**

```bash
python -m tests.test_deterministic
```

**To run the Stochastic tests:**

```bash
python -m tests.test_stochastic
```

*(Note: Ensure you are in the project's root directory when running tests).*

## Project Structure

  * `src/`: Contains the core logic for calculations.
      * `customers.py`: Functions for D/D/1 $n(t)$ calculations.
      * `waiting.py`: Functions for D/D/1 $W_q(n)$ calculations.
      * `stochastic_customers.py`: Functions for M/M/1 performance metrics.
  * `helpers/`: Helper functions for validations and intermediate calculations.
  * `tests/`: Unit tests for the project.
  * `main.py`: The CLI entry point for the user.
