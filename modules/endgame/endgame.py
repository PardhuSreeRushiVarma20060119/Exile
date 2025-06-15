# modules/endgame.py (Exile-SafeWork with bonus ideas)

import os
import time
import json
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

# Constants and Storage
INFECTIONS_FILE = "sim_infections.json"
console = Console()

sim_processes = [
    {"pid": 2234, "name": "explorer.exe", "user": "victim", "priv": "Medium"},
    {"pid": 4561, "name": "svchost.exe", "user": "SYSTEM", "priv": "High"},
    {"pid": 1029, "name": "notepad.exe", "user": "victim", "priv": "Low"},
]

# Utils

def load_infections():
    if os.path.exists(INFECTIONS_FILE):
        with open(INFECTIONS_FILE, "r") as f:
            return json.load(f)
    return []

def save_infection(pid, technique):
    infections = load_infections()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    infections.append({"pid": pid, "technique": technique, "timestamp": timestamp})
    with open(INFECTIONS_FILE, "w") as f:
        json.dump(infections, f, indent=4)

def beacon_console():
    with Live(console=console, refresh_per_second=4) as live:
        for _ in range(20):
            panel = Panel(
                f"[bold green]Beacon Emulation[/bold green]\nTarget Active: svchost.exe\nHeartbeat: OK\nStatus: Listening...",
                title="[red]Exile Fake Beacon",
                border_style="blue"
            )
            live.update(panel)
            time.sleep(1)

# Simulation Functions

def simulate_process_hollowing(pid):
    console.print(f"\n[cyan]Simulating Process Hollowing on PID {pid}...[/cyan]")
    time.sleep(1)
    console.print("[+] Stub injected.")
    time.sleep(1)
    console.print("[+] Code mapped to memory (0xAABBCCDD).")
    time.sleep(1)
    console.print("[✓] Control transferred. Hollowing complete.\n")
    save_infection(pid, "Process Hollowing")

def simulate_dll_injection(pid):
    console.print(f"\n[cyan]Simulating DLL Injection on PID {pid}...[/cyan]")
    time.sleep(1)
    console.print("[+] DLL loaded from dummy path.")
    time.sleep(1)
    console.print("[✓] Injection simulated.\n")
    save_infection(pid, "DLL Injection")

def simulate_in_memory_exec():
    console.print("\n[cyan]Simulating In-Memory Execution...[/cyan]")
    time.sleep(1)
    console.print("[+] Payload loaded into memory (0xDEADBEEF).")
    time.sleep(1)
    console.print("[✓] Executed safely.\n")
    save_infection("N/A", "In-Memory Execution")

def simulate_av_evasion():
    console.print("\n[cyan]Simulating AV/EDR Evasion...[/cyan]")
    steps = [
        "API unhooking (simulated)",
        "String encryption",
        "LOLBins used for staging",
        "Syscall redirection (emulated)"
    ]
    for step in steps:
        time.sleep(0.8)
        console.print(f"[+] {step}")
    console.print("[✓] AV evasion complete.\n")

def list_targets():
    table = Table(title="Simulated Target Processes")
    table.add_column("PID", justify="center")
    table.add_column("Process Name")
    table.add_column("User")
    table.add_column("Privilege")

    for proc in sim_processes:
        table.add_row(str(proc['pid']), proc['name'], proc['user'], proc['priv'])
    console.print(table)

def show_infection_log():
    infections = load_infections()
    table = Table(title="Simulated Infections Log")
    table.add_column("PID")
    table.add_column("Technique")
    table.add_column("Timestamp")
    for inf in infections:
        table.add_row(str(inf['pid']), inf['technique'], inf['timestamp'])
    console.print(table)

# Shellcode Lab (Emulated)
def shellcode_lab():
    console.print("\n[cyan]Shellcode Laboratory[/cyan]")
    shellcodes = [
        {"name": "Sim MessageBox Shellcode", "hex": "\x90\x90\x90\xCC"},
        {"name": "NOP Slide Shellcode", "hex": "\x90" * 20},
        {"name": "Sim Bind Shellcode", "hex": "\xCC\xCC\xCC\xCC"},
    ]
    table = Table(title="Fake Shellcode Samples")
    table.add_column("Name")
    table.add_column("Hex Preview")
    for sc in shellcodes:
        table.add_row(sc["name"], sc["hex"][:20] + "...")
    console.print(table)
    input("\n[>] Press Enter to return...")

# Payload Laboratory (Emulated)
def payload_lab():
    console.print("\n[cyan]Payload Laboratory[/cyan]")
    payloads = [
        {"name": "Reverse Shell Sim", "desc": "Pretend reverse connection"},
        {"name": "Bind Shell Sim", "desc": "Pretend bind socket"},
        {"name": "Download & Exec Sim", "desc": "Pretend download to temp"},
    ]
    table = Table(title="Payload Templates")
    table.add_column("Name")
    table.add_column("Description")
    for p in payloads:
        table.add_row(p["name"], p["desc"])
    input("\n[>] Press Enter to return...")

# Menu

def endgame_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n[bold red]EXILE-SAFEWORK | ENDGAME MODULE[/bold red]\n")
        console.print("[1] Simulate Process Hollowing")
        console.print("[2] Simulate DLL Injection")
        console.print("[3] Simulate In-Memory Execution")
        console.print("[4] Simulate AV/EDR Evasion")
        console.print("[5] View Simulated Targets")
        console.print("[6] Show Infection Log")
        console.print("[7] Launch Fake Beacon Console")
        console.print("[8] Shellcode Laboratory")
        console.print("[9] Payload Laboratory")
        console.print("[0] Back")

        choice = input(">> ").strip()

        if choice == "1":
            list_targets()
            pid = input("Enter PID to simulate hollowing: ").strip()
            simulate_process_hollowing(pid)
            input("\nPress Enter to continue...")
        elif choice == "2":
            list_targets()
            pid = input("Enter PID to simulate DLL injection: ").strip()
            simulate_dll_injection(pid)
            input("\nPress Enter to continue...")
        elif choice == "3":
            simulate_in_memory_exec()
            input("\nPress Enter to continue...")
        elif choice == "4":
            simulate_av_evasion()
            input("\nPress Enter to continue...")
        elif choice == "5":
            list_targets()
            input("\nPress Enter to continue...")
        elif choice == "6":
            show_infection_log()
            input("\nPress Enter to continue...")
        elif choice == "7":
            beacon_console()
            input("\nPress Enter to continue...")
        elif choice == "8":
            shellcode_lab()
        elif choice == "9":
            payload_lab()
        elif choice == "0":
            break
        else:
            console.print("[!] Invalid option.", style="bold red")
            time.sleep(1)

def run_endgame():
    """Function to run endgame simulation - compatible with dispatch system"""
    endgame_menu()

if __name__ == "__main__":
    run_endgame()
