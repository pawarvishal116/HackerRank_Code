import subprocess

try:
    subprocess.run(
        ["python3", "-c", "import time; time.sleep(20)"],
        timeout=5,  # Set a timeout of 5 seconds
        check=True  # Raises CalledProcessError if the command returns a non-zero exit status
    )

except subprocess.TimeoutExpired:
    print("Command timed out")

'''
What happens?
1. Python starts the external process.
2. The process starts sleeping for 20 seconds.
3. Subprocess waits for a maximum of 5 seconds.
4. After 5 seconds, it terminates the timed-out process and raises TimeoutExpired.
5. Your exception handler prints the message.
'''