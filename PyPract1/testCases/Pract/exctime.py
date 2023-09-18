import time
#10.Implement a decorator that quantifies and returns the execution time of any function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

# Example usage
@measure_time
def some_function():
    time.sleep(5)
    print("Function executed.")

some_function()
