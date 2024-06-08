import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def reimann_integral(a, b, N):
    dx = (b - a) / N
    integral = 0
    for i in range(N):
        x_i = a + i * dx
        integral += f(x_i) * dx
    return integral

def calculate_error(true_value, approx_value):
    return np.sqrt(np.mean((true_value - approx_value)**2))

if __name__ == "__main__":
    true_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]

    for N in N_values:
        start_time = time.time()
        approx_pi = reimann_integral(0, 1, N)
        execution_time = time.time() - start_time

        error = calculate_error(true_pi, approx_pi)

        print(f"For N = {N}:")
        print(f"Approximated Pi: {approx_pi}")
        print(f"Root Mean Square Error: {error}")
        print(f"Execution Time: {execution_time} seconds")
        print()
