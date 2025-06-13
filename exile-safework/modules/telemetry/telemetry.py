# telemetry.py - Exile-SafeWork v1.0.4
# Safe Telemetry Monitoring Emulator

import random
import time
from datetime import datetime

class Telemetry:
    def __init__(self):
        self.metrics = []

    def collect_metrics(self):
        print("[+] Collecting simulated telemetry metrics...")
        metric = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cpu_usage": f"{random.randint(1, 50)}%",
            "ram_usage": f"{random.randint(100, 800)}MB",
            "disk_activity": f"{random.randint(10, 90)} ops/sec",
            "net_activity": f"{random.randint(50, 300)} Kbps"
        }
        self.metrics.append(metric)
        print(f"[✓] Captured at {metric['timestamp']}")

    def print_report(self):
        print("\n=== Telemetry Report ===")
        if not self.metrics:
            print("[!] No telemetry data collected.")
            return
        for metric in self.metrics:
            print(f"[{metric['timestamp']}] CPU: {metric['cpu_usage']} | RAM: {metric['ram_usage']} | DISK: {metric['disk_activity']} | NET: {metric['net_activity']}")

if __name__ == "__main__":
    print("=== Exile SafeWork: Telemetry Simulator ===")
    t = Telemetry()
    while True:
        print("\n1. Collect Metrics")
        print("2. Show Telemetry Report")
        print("3. Exit")
        choice = input("Select option: ")
        if choice == '1':
            t.collect_metrics()
        elif choice == '2':
            t.print_report()
        elif choice == '3':
            break
        else:
            print("[!] Invalid selection")
