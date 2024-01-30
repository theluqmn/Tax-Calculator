import platform, os
os_system = platform.system()
if os_system == "Windows":
    os.system("cls")
else:
    os.system("clear")