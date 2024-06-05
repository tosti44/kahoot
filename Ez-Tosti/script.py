from scripts.sprint import sprint
from scripts.colors import ran, y, r, g, c
from subprocess import call
import time
import os

print(f"{g}████████╗  █████╗   ██████╗ ████████╗ ██╗")
print(f"{g}╚══██╔══╝ ██╔══██╗ ██╔════╝ ╚══██╔══╝ ██║")
print(f"{g}   ██║    ██║  ██║ ╚█████╗     ██║    ██║")
print(f"{g}   ██║    ██║  ██║   ╚═══██╗   ██║    ██║")
print(f"{g}   ██║    ╚█████╔╝  ██████╔╝   ██║    ██║")
print(f"{g}   ╚═╝     ╚════╝   ╚═════╝    ╚═╝    ╚═╝")
time.sleep(2)
sprint(f"{g}Please choose 1 or 2{g}")
print(" ")
print(f"{g}[1] How to use")
print(" ")
print(f"{g}[2] answers{g}")
print(" ")
choice = input("")


if choice == "1":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/HTU.py"])

if choice == "2":
    print(" ")
    print("Starting...")
    time.sleep(1)
    print("\n" * 64)  
    call(["python", "Kahoot/kahoot.py"])

