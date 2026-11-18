import subprocess

process = subprocess.Popen(["python", "--version"])

print("Next statement")

process.wait()

print("Process completed")


'''
Here:
- Popen() starts the external process.
- Python can continue executing other statements.
- wait() waits until the process finishes.
Use Popen() when you need more control over a running process, such as interacting with it while it runs or managing multiple processes.


Feature	                                        run()	                Popen()
Starts external process	                        Yes	                     Yes
Waits automatically	                            Yes	                     No
Returns	                                    CompletedProcess	      Popen object
Process management	                            Simpler	               More control
Beginner-friendly	                            Yes	                   More advanced
'''