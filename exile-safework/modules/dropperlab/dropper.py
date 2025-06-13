import os
import shutil
import time
import random

SIMULATED_LOCATIONS = [
    os.path.expanduser("~/AppData/Roaming"),
    os.path.expanduser("~/AppData/Local/Temp"),
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/.config"),
]

def simulate_dropper(payload_path, destination_dir):
    try:
        if not os.path.isfile(payload_path):
            print("[!] Payload file does not exist.")
            return

        if not os.path.isdir(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

        filename = os.path.basename(payload_path)
        target_path = os.path.join(destination_dir, filename)

        shutil.copyfile(payload_path, target_path)

        print(f"[+] Payload successfully dropped at: {target_path}")
        simulate_persistence(target_path)
        simulate_execution(target_path)

    except Exception as e:
        print(f"[!] Error: {e}")

def simulate_persistence(path):
    print(f"[*] Simulating persistence (no real registry edits or service creation)...")
    techniques = [
        f"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run -> {os.path.basename(path)}",
        f"Startup Folder Shortcut -> {os.path.basename(path)}",
        f"Scheduled Task (simulated)",
        f"Crontab Entry (Linux style emulation)",
    ]
    time.sleep(1)
    print(f"[+] Technique used: {random.choice(techniques)}")

def simulate_execution(path):
    print(f"[*] Simulating execution of {os.path.basename(path)}...")
    time.sleep(1)
    print("[+] Simulated process launch (not actually run)")

def dropper_menu():
    print("\n=== EXILE-SAFEWORK :: DROPPER LAB ===")
    payload = input("Enter path to dummy payload (e.g., test.exe): ").strip()
    
    print("\nWhere to simulate drop?")
    for i, loc in enumerate(SIMULATED_LOCATIONS):
        print(f" [{i}] {loc}")

    try:
        choice = int(input(">> "))
        if choice not in range(len(SIMULATED_LOCATIONS)):
            raise ValueError
        dest_dir = SIMULATED_LOCATIONS[choice]
    except ValueError:
        print("[!] Invalid option.")
        return

    simulate_dropper(payload, dest_dir)

if __name__ == "__main__":
    dropper_menu()
    print("\n[+] Dropper simulation complete.")
    print("[+] Exiting.")
    exit()
    