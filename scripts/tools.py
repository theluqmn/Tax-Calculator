import platform, os

def Clear():
    os_system = platform.system()
    if os_system == "Windows":
        os.system("cls")
    else:
        os.system("clear")