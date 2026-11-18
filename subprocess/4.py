import subprocess

subprocess.run("python3 --version", shell=True)

#shell=True allows you to pass the command as a single string, 
# which is then executed through the shell. 
# This can be useful for commands that include shell features like pipes or redirection. 
# However, using shell=True can pose security risks if you're passing user input directly into the command, 
# so it should be used with caution.

