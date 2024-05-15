from timeit import timeit
# import timeit() method from timeit module

code = """[4, 2, 3, 1, 5].sort()"""

execution_time =timeit(code, number=1)

print(execution_time)