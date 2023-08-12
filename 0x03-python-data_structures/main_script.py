#!/usr/bin/python3
import subprocess
import timeit

# Run my_script.py and measure its execution time
code_to_run = "subprocess.run(['python3', '2-main.py'], check=True)"

execution_time = timeit.timeit(stmt=code_to_run, setup="import subprocess", number=10)

print(f"Execution time: {execution_time:.6f} seconds")
