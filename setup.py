import os
import sys
# import requests
import subprocess
# import getpass
# import shutil


def install_python_and_upgrade_pip():
    subprocess.call("yum update -y", shell=True)
    subprocess.call("yum install openssl-devel bzip2-devel libffi-devel -y", shell=True)
    subprocess.call("yum groupinstall 'Development Tools' -y", shell=True)
    subprocess.call("yum install wget -y", shell=True)
    subprocess.call("wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz", shell=True)
    subprocess.call("tar -xzf Python-3.10.2.tgz", shell=True)
    os.chdir("Python-3.10.2")
    subprocess.call("./configure --enable-optimizations", shell=True)
    subprocess.call("make altinstall", shell=True)
    subprocess.call("python3.10 -V", shell=True)
    subprocess.call(["python3", "-m", "pip", "install", "--upgrade", "pip"])


def move_files(dst_dir):
    files = ['latest.py', 'constucted.py', 'bigVar.py', 'CreateUser.py', 'functions.py']
    # Move each file to the destination directory
    for file in files:
        dst_file = os.path.join(dst_dir, file)
        os.rename(file, dst_file)


# def get_private_github_repo(repo_url, repo_directory):
#     # Get the username and password for the private Github repository
#     username = input("Enter Github username: ")
#     password = input("Enter Github password: ")
#
#     # Use the credentials to access the private Github repository
#     auth = (username, password)
#     response = requests.get(repo_url, auth=auth)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Clone the repository to the specified directory
#         subprocess.run(["git", "clone", repo_url, repo_directory], check=True)
#     else:
#         print(f"Error accessing repository, status code: {response.status_code}")


# Create folders
folder_list = [
    '/usr/include/pxmailer',
    '/usr/include/pxmailer/images',
    '/usr/include/pxmailer/attached',
    '/usr/include/pxmailer/leads',
    '/usr/include/pxmailer/licences',
]

for folder in folder_list:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"{folder} created successfully")

# Create files
file_list = [
    '/usr/bin/spam',
    '/usr/bin/pxuser',
    # '/usr/include/pxmailer/latest.py',
    # '/usr/include/pxmailer/constructed.py',
    # '/usr/include/pxmailer/functions.py',
    # '/usr/include/pxmailer/bigVar.py',
    # '/usr/include/pxmailer/CreateUser.py',
]

for file in file_list:
    open(file, 'a').close()

move_files('/usr/include/pxmailer/')
# get_private_github_repo('https://github.com/Obimba/Px-Mailer.git', '/usr/include/pxmailer/')

# Give permissions to folders
folder_permissions = [
    '/usr/include/pxmailer/attached',
    '/usr/include/pxmailer/leads',
    '/usr/include/pxmailer/licences',
]

for folder in folder_permissions:
    os.chmod(folder, 0o777)

# Give permissions to files
file_permissions = [
    '/usr/include/pxmailer/bigVar.py',
    '/usr/include/pxmailer/functions.py',
    '/usr/include/pxmailer/CreateUser.py',
    '/usr/include/pxmailer/constructed.py',
    '/usr/include/pxmailer/latest.py',
    '/usr/bin/pxuser',
    '/usr/bin/spam',
]

for file in file_permissions:
    os.chmod(file, 0o777)

# Install required packages
subprocess.call(["yum", "update", "-y"])
subprocess.call(["yum", "install", "-y", "python3"])
subprocess.call(["sudo", "yum", "install", "epel-release", "-y"])
subprocess.call(["sudo", "yum", "install", "python-pip", "-y"])
subprocess.call(["yum", "install", "git", "-y"])
subprocess.call(["git", "clone", "https://github.com/reingart/pyfpdf.git"])
os.chdir("pyfpdf")
subprocess.call(["python", "setup.py", "install"])
subprocess.call(["pip", "install", "fpdf"])
subprocess.call(["yum", "install", "dos2unix"])

# Perform dos2unix on specified files
dos2unix_list = [
    '/usr/include/pxmailer/latest.py',
    '/usr/include/pxmailer/constructed.py',
    '/usr/include/pxmailer/bigVar.py',
    '/usr/include/pxmailer/CreateUser.py',
    '/usr/include/pxmailer/functions.py',
    '/usr/bin/spam',
    '/usr/bin/pxuser',
]

for file in dos2unix_list:
    subprocess.call(["dos2unix", file])

# Write content to /usr/bin/spam
with open("/usr/bin/spam", "w") as f:
    f.write("#!/bin/bash\npython3 /usr/include/pxmailer/latest.py")


# Make /usr/bin/spam file executable
os.chmod("/usr/bin/spam", 0o777)

# Write content to /usr/bin/pxuser
with open("/usr/bin/pxuser", "w") as f:
    f.write("#!/bin/bash\npython3 /usr/include/pxmailer/CreateUser.py")

# Make /usr/bin/pxuser file executable
os.chmod("/usr/bin/pxuser", 0o777)

# Convert files to Unix line endings

subprocess.call(["dos2unix", "/usr/include/pxmailer/latest.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/constructed.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/bigVar.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/CreateUser.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/functions.py"])
subprocess.call(["dos2unix", "/usr/bin/spam"])
subprocess.call(["dos2unix", "/usr/bin/pxuser"])

# Install python3
if sys.version_info[0] < 3:
    subprocess.call(["yum", "update", "-y"])
    subprocess.call(["yum", "install", "-y", "python3"])

# Install pip
subprocess.call(["sudo", "yum", "install", "epel-release"])
subprocess.call(["sudo", "yum", "install", "python-pip"])

# Install git
subprocess.call(["yum", "install", "git", "-y"])

# Install fpdf
subprocess.call(["git", "clone", "https://github.com/reingart/pyfpdf.git"])
os.chdir("pyfpdf")
subprocess.call(["python", "setup.py", "install"])
subprocess.call(["python3", "setup.py", "install"])
subprocess.call(["pip", "install", "fpdf"])
subprocess.call(["pip3", "install", "fpdf"])

# Install dos2unix
subprocess.call(["yum", "install", "dos2unix"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/latest.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/constructed.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/bigVar.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/CreateUser.py"])
subprocess.call(["dos2unix", "/usr/include/pxmailer/functions.py"])
subprocess.call(["dos2unix", "/usr/bin/spam"])
subprocess.call(["dos2unix", "/usr/bin/pxuser"])
install_python_and_upgrade_pip()
subprocess.call(["pip3", "install", "bcrypt"])
os.remove("/root/mailer.zip")
os.remove(__file__)