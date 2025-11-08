import subprocess
import signal
import webbrowser
import time
import os

def find_roblox():
    for line in os.popen("tasklist"):
        if "RobloxPlayerBeta.exe" in line:
            return(int(line.split()[1]))
    return None

def launch_roblox():
    webbrowser.open("roblox://navigation/home")
    roblox = find_roblox()
    while not roblox:
        time.sleep(0.5)
        roblox = find_roblox()
    return(roblox)

scripts = os.listdir(os.path.abspath(os.path.dirname(__file__) + "/Scripts"))
print("0: None")
for i, file in enumerate(scripts, 1):
    print(f"{i}: {file}")

while True:
    choice = int(input("Select a script: "))
    chosen_script_args = []

    if 1 <= choice <= len(scripts):
        chosen_script_args = ["-s", os.path.abspath(os.path.dirname(__file__) + "/Scripts" + f"/{scripts[choice-1]}")]
        break
    elif choice == 0:
        break
    else: 
        print("Invalid number")
        continue

initial_process = find_roblox()
if initial_process:
    print("For this program to function it needs to close your current roblox process")
    input("Enter any key to continue")
    os.kill(initial_process, signal.SIGILL)
    time.sleep(0.5)
os.kill(launch_roblox(), signal.SIGILL)

subprocess.run(["python", os.path.abspath(os.path.dirname(__file__) + "/certificate-loader.py")], check=True)
subprocess.Popen(["cmd", "/c", "start", "mitmproxy", *chosen_script_args,"--mode", "local:RobloxPlayerBeta.exe", "--set", "confdir=Certificates\\"])   

launch_roblox()