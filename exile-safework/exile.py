#!/usr/bin/env python3
import sys
from core.banner import show_banner
from core.dispatch import dispatch_command

def main():
    show_banner()
    while True:
        try:
            cmd = input("Exile> ").strip()
            if cmd in ("exit", "quit"):
                print("[*] Exiting Exile-SafeWork.")
                break
            dispatch_command(cmd)
        except KeyboardInterrupt:
            print("\n[!] Interrupted.")
            break

if __name__ == "__main__":
    main()
