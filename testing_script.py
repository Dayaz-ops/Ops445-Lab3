# Import the os module
import os

# Issue some Linux system commands using os.system() and capture their return value
os.system('ls')
os.system('whoami')
os.system('ifconfig')

# Compare the output with return values
ls_return = os.system('ls')
print('The contents of ls_return:', ls_return)

whoami_return = os.system('whoami')
print('The contents of whoami_return:', whoami_return)

ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:', ifconfig_return)

# Test the ipconfig command on Linux (should produce an error)
ipconfig_return = os.system('ipconfig')
print('The contents of ipconfig_return:', ipconfig_return)
