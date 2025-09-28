#!/usr/bin/env python3
import sys
from core.banner import show_banner
from core.dispatch import dispatch_command

def display_menu():
    print("""
Available Modules:
  [1] dropperlab     - Create and manage droppers
  [2] stage1         - Initial access/stager modules
  [3] stage2         - Privilege escalation, in-memory tools
  [4] endgame        - Post-exploitation tools
  [5] payloadlab     - Build mock payloads
  [6] telemetry      - Emulated monitoring/logging
  [7] crypter        - Emulated payload obfuscation
  [8] guard          - Detection evasion logics (mock)
  [9] vault          - Secure simulated storage
 [10] sharedspace    - Simulated sessions for collaboration
 [11] dashboard      - Status & simulated analytics
 [12] exit/quit      - Exit Exile-SafeWork
""")

def main():
    show_banner()
    while True:
        try:
            display_menu()
            cmd = input("Exile> ").strip().lower()
            if cmd in ("exit", "quit", "12"):
                print("[*] Exiting Exile-SafeWork.")
                break

            # Accept both names and numbers
            cmd_map = {
                "1": "dropperlab",
                "2": "stage1",
                "3": "stage2",
                "4": "endgame",
                "5": "payloadlab",
                "6": "telemetry",
                "7": "crypter",
                "8": "guard",
                "9": "vault",
                "10": "sharedspace",
                "11": "dashboard"
            }

            # Normalize to command string
            selected = cmd_map.get(cmd, cmd)
            dispatch_command(selected)

        except KeyboardInterrupt:
            print("\n[!] Interrupted.")
            break

if __name__ == "__main__":
    main()
