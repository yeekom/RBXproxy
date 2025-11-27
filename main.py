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

addons_folder = os.path.abspath(os.path.dirname(__file__) + "/Addons")
addons = [name for name in os.listdir(addons_folder) if os.path.isdir(addons_folder + f"/{name}")]
print("Select a script to run with Mitmproxy")
print("0: None")
for i, file in enumerate(addons, 1):

    print(f"{i}: {file}")

while True:
    choice = int(input("Select a addon: "))
    chosen_script_args = []

    if 1 <= choice <= len(addons):
        chosen_script_args = ["-s", os.path.abspath(os.path.dirname(__file__) + "/Addons" + f"/{addons[choice-1]}" + "/addon.py")]
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
subprocess.Popen(["cmd", "/c", "start", "mitmproxy", *chosen_script_args,"--mode", "local:RobloxPlayerBeta.exe", "--set", f"confdir={os.path.abspath(os.path.dirname(__file__) + "/Certificates")}"])   
