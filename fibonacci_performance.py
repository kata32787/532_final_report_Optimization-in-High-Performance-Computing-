import time
from functools import lru_cache

# Without optimization
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(fibonacci(35))
end = time.time()
print(f"Execution Time Without Caching: {end - start:.4f} seconds")

# With LRU Cache Optimization
@lru_cache(maxsize=None)
def fibonacci_optimized(n):
    if n <= 1:
        return n
    return fibonacci_optimized(n-1) + fibonacci_optimized(n-2)

start = time.time()
print(fibonacci_optimized(35))
end = time.time()
print(f"Execution Time With Caching: {end - start:.4f} seconds")
