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
sprint(f"{g}Please choose 1, 2 or 3{g}")
print(" ")
print(f"{g}[1] How to use")
print(" ")
print(f"{g}[2] answers-new{g}")
print(" ")
print(f"{g}[3] answers-old{g}")
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
    call(["python", "Kahoot/kahootnew.py"])

if choice == "3":
    print(" ")
    print("Starting...")
    time.sleep(1)
    print("\n" * 64)  
    call(["python", "Kahoot/kahootold.py"])
