from timeit import timeit
# import timeit() method from timeit module
setup_code = "from math import factorial"

statement = """
for i in range(10):
    factorial(i)
"""

print(f"Execution time is: {timeit(setup = setup_code, stmt = statement, number = 10000000)}")