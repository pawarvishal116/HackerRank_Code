import subprocess

try:
    result = subprocess.run(
        ["python3", "-c", "print(10 / 0)"],
        check=True                  # Raises CalledProcessError if the command returns a non-zero exit status
    )

    print("Command completed")

except subprocess.CalledProcessError as e:
    print("Command failed")
    print("Return code:", e.returncode)


'''
CalledProcessError = Command ran, but failed.
FileNotFoundError = Command executable wasn't found.
PermissionError = Command couldn't be executed because of permissions.
'''