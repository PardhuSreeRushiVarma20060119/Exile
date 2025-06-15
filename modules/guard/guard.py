import time
import threading
import random
import os

simulated_behaviors = [
    "Unusual memory allocation in explorer.exe",
    "Suspicious process injection attempt in svchost.exe",
    "Encoded PowerShell command execution",
    "Remote thread creation detected",
    "Suspicious child process spawned: cmd.exe from Outlook.exe",
    "DLL loaded from unusual directory",
    "Base64 shellcode pattern identified in memory dump",
    "Parent-child process anomaly: msword.exe → rundll32.exe"
]

alert_log = []

def generate_fake_telemetry():
    while True:
        time.sleep(random.randint(5, 10))
        event = random.choice(simulated_behaviors)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        alert_log.append(f"[{timestamp}] ALERT: {event}")
        if len(alert_log) > 20:
            alert_log.pop(0)

def view_alert_log():
    print("\n[+] Telemetry Alerts (Simulated)")
    print("-" * 60)
    for entry in alert_log:
        print(entry)
    print("-" * 60)

def export_alerts():
    filename = f"exile_telemetry_log.txt"
    with open(filename, 'w') as f:
        for entry in alert_log:
            f.write(entry + "\n")
    print(f"[✓] Log exported to {filename}")

def monitor_guard():
    threading.Thread(target=generate_fake_telemetry, daemon=True).start()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[91m[ EXILE-SAFEWORK | GUARD MODULE ]\033[0m\n")
        print("[1] View Active Alerts")
        print("[2] Export Alert Log")
        print("[0] Back")

        choice = input(">> ").strip()
        if choice == "1":
            view_alert_log()
            input("\nPress Enter to return...")
        elif choice == "2":
            export_alerts()
            input("\nPress Enter to return...")
        elif choice == "0":
            break
        else:
            print("[!] Invalid option.")
            time.sleep(1)

def guard_menu():
    """Function for guard menu - compatible with dispatch system"""
    monitor_guard()

if __name__ == "__main__":
    guard_menu()
