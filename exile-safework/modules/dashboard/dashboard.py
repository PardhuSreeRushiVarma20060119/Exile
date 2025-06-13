import time
import random
import os

dummy_targets = [
    {"ip": "192.168.1.10", "os": "Windows 10", "status": "Online", "privilege": "User"},
    {"ip": "192.168.1.23", "os": "Debian 11", "status": "Compromised", "privilege": "Root"},
    {"ip": "10.0.0.45", "os": "Windows Server 2019", "status": "Offline", "privilege": "Unknown"},
]

logs = []

def simulate_log():
    fake_activities = [
        "Generated encrypted payload",
        "Simulated process hollowing",
        "Fake connection to 192.168.1.23:4444",
        "Dummy beacon signal sent",
        "Staged dropper emulated",
        "UAC bypass (simulated) failed",
        "Telemetry sync complete",
    ]
    return random.choice(fake_activities)

def display_targets():
    print("\n[+] Active Hosts (Emulated):")
    print("-" * 60)
    print(f"{'IP Address':<20}{'OS':<20}{'Privilege':<10}{'Status'}")
    print("-" * 60)
    for t in dummy_targets:
        print(f"{t['ip']:<20}{t['os']:<20}{t['privilege']:<10}{t['status']}")
    print("-" * 60)

def display_logs():
    print("\n[+] Telemetry Logs (Safe Emulation):")
    for log in logs[-10:]:
        print(f"[*] {log}")
    print("-" * 60)

def dashboard_loop():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[91m" + "[ EXILE-SAFEWORK | DASHBOARD MODULE ]\n" + "\033[0m")
        display_targets()

        # Simulate a new log every cycle
        logs.append(f"{time.strftime('%H:%M:%S')} - {simulate_log()}")
        display_logs()

        print("\nOptions: [R]efresh | [0] Back to Main Menu")
        choice = input(">> ").strip().lower()

        if choice == "0":
            break
        elif choice != "r":
            print("[!] Invalid option.")
            time.sleep(1)

def dashboard_menu():
    """Function for dashboard menu - compatible with dispatch system"""
    dashboard_loop()

if __name__ == "__main__":
    dashboard_menu()