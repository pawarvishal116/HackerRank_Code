import subprocess

commands = [
    ["python3", "--version"],
    ["git", "--version"],
    ["pwd"]
]

for command in commands:

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print("Command:", command)
    print("Output:", result.stdout)
    print("Return code:", result.returncode)
    print("----------------------")