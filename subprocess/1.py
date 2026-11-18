import subprocess

'''Important: Each element in the list is treated as a separate command-line argument.

You don't need to manually handle spaces or quotation marks in arguments.
'''
subprocess.run(["python3", "--version"])    # provide list elements as command-line arguments

subprocess.run(["python3", "hello.py"])

##########################################

'''
Let's understand the two parameters:
- capture_output=True: Captures the output instead of displaying it directly in the terminal.
- text=True: Converts the captured output from bytes into a normal Python string.
'''

result = subprocess.run(
    ["python3", "--version"],
    capture_output=True,
    text=True
)


print(result) # CompletedProcess(args=['python3', '--version'], returncode=0, stdout='Python 3.13.15\n', stderr='')
print(result.stdout) # Python 3.13.15
print(result.stderr) # (empty string)
print(result.returncode) # 0   # 0 indicates that the command executed successfully without any errors.

##########################


result = subprocess.run(
    ["python3", "-c", "print(10 / 0)"],
    capture_output=True,
    text=True
)

print(result) # CompletedProcess(args=['python3', '-c', 'print(10 / 0)'], returncode=1, stdout='', stderr='Traceback (most recent call last):\n  File "<string>", line 1, in <module>\nZeroDivisionError: division by zero\n')
print("Output:", result.stdout)
print("Error:", result.stderr)
print("Return Code:", result.returncode) # 1   # Non-zero return code indicates an error occurred during execution.

###############################