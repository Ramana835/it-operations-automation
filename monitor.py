import os

print("Checking Disk Usage...\n")
os.system("df -h")

print("\nChecking Memory Usage...\n")
os.system("free -m")

print("\nSystem Health Check Completed ✅")
