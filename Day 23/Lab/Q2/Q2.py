import math
import time
import sys
from multiprocessing import Pool, cpu_count

# Fix for Python 3.11+ large integer string conversion limit
sys.set_int_max_str_digits(10_000_000)

# Function to calculate factorial
def calculate_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    numbers = [50000, 60000, 55000, 45000, 70000]

    print("CPU Cores Available:", cpu_count())
    print("-" * 60)

    # =====================================================
    # 1️⃣ Sequential Computation
    # =====================================================
    start_time = time.time()

    sequential_results = []
    for n in numbers:
        sequential_results.append(calculate_factorial(n))

    sequential_time = time.time() - start_time

    print("Sequential Execution Time:", sequential_time)
    print("-" * 60)

    # =====================================================
    # 2️⃣ Multiprocessing Computation
    # =====================================================
    start_time = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(calculate_factorial, numbers)

    multiprocessing_time = time.time() - start_time

    print("Multiprocessing Execution Time:", multiprocessing_time)
    print("-" * 60)

    # =====================================================
    # 3️⃣ Print Factorial Results
    # (Printing digit count instead of full factorial)
    # =====================================================
    print("Factorial Results:")
    for i in range(len(numbers)):
        print(f"Factorial of {numbers[i]} has {len(str(parallel_results[i]))} digits")

    print("-" * 60)

    # =====================================================
    # 4️⃣ Performance Comparison
    # =====================================================
    if multiprocessing_time < sequential_time:
        print("Result: Multiprocessing is Faster")
    else:
        print("Result: Sequential is Faster")
