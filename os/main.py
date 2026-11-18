import os
import shutil

current_directory = os.getcwd()
print("Current working directory:", current_directory)

#changes_directory = os.chdir("/path/to/directory")  # Change to your desired directory
#new_directory = os.getcwd()
#print("New working directory:", new_directory)

###############

files = os.listdir(current_directory)
print("Files and directories in the current directory:")
for item in files:
    print(item)

for file in files:
    if os.path.isfile(file):
        print(f"{file} is a file.")
    elif os.path.isdir(file):
        print(f"{file} is a directory.")

###############################

os.mkdir("new_directory")  # Create a new directory named "new_directory"
os.rmdir("new_directory")  # Remove the directory named "new_directory"

os.rename("old_name.txt", "new_name.txt")  # Rename a file from "old_name.txt" to "new_name.txt"

os.remove("file_to_delete.txt")  # Delete a file named "file_to_delete.txt"

os.path.exists("file_or_directory")  # Check if a file or directory exists

os.path.join("directory", "file.txt")  # Join directory and file name to create a full path

os.path.abspath("file_or_directory")  # Get the absolute path of a file or directory

os.path.basename("/path/to/file.txt")  # Get the base name (file name) from a path

os.path.dirname("/path/to/file.txt")  # Get the directory name from a path

os.path.splitext("file.txt")  # Split the file name and extension

os.path.getsize("file.txt")  # Get the size of a file in bytes

os.path.getmtime("file.txt")  # Get the last modification time of a file

os.path.getctime("file.txt")  # Get the creation time of a file

os.path.isdir("directory")  # Check if a path is a directory

os.path.isfile("file.txt")  # Check if a path is a file

os.path.islink("link")  # Check if a path is a symbolic link

os.path.realpath("link")  # Get the real path of a symbolic link

os.cpu_count()  # Get the number of CPUs in the system

os.getlogin()  # Get the name of the user logged in to the controlling terminal

os.getpid()  # Get the current process ID   

os.getppid()  # Get the parent process ID

os.environ  # Access environment variables as a dictionary

os.environ.get("HOME")  # Get the value of the HOME environment variable

os.environ["MY_VARIABLE"] = "value"  # Set an environment variable

os.environ.pop("MY_VARIABLE", None)  # Remove an environment variable if it exists

os.makedirs("nested/directory/structure", exist_ok=True)  # Create nested directories, ignoring if they already exist

#######################
import shutil
shutil.copy("source.txt", "destination.txt")  # Copy a file from source to destination
shutil.copytree("source_directory", "destination_directory")  # Copy an entire directory tree
shutil.move("source.txt", "destination.txt")  # Move a file or directory to a new location
shutil.rmtree("directory_to_delete")  # Remove an entire directory tree     
shutil.disk_usage("/")  # Get disk usage statistics for the root directory
shutil.chown("file.txt", user="username", group="groupname")  # Change the owner and group of a file or directory           
shutil.which("python3")  # Find the path to an executable in the system's PATH
shutil.get_terminal_size()  # Get the size of the terminal window
shutil.unpack_archive("archive.zip", "destination_directory")  # Unpack an archive file to a destination directory
shutil.make_archive("archive", "zip", "source_directory")  # Create an archive file from a source directory
shutil.get_archive_formats()  # Get a list of supported archive formats
shutil.get_unpack_formats()  # Get a list of supported unpack formats
shutil.get_terminal_size()  # Get the size of the terminal window
shutil.get_terminal_size(fallback=(80, 24))  # Get the size of the terminal window with a fallback value
shutil.get_terminal_size().columns  # Get the number of columns in the terminal window
