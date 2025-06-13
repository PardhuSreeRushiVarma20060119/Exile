# payload.py - Exile-SafeWork v1.0.4
# Safe Payload Emulator Module

import base64
import os
import random
import string

def generate_safe_payload(type="reverse_shell"):
    """
    Simulates payload generation (for learning/testing only).
    """
    print("[+] Generating safe payload...")
    if type == "reverse_shell":
        code = """
        # Safe Reverse Shell Simulation
        import socket
        def connect():
            print('[SIMULATION] Connecting to attacker...')
            print('[SIMULATION] Sending shell-like behavior logs...')
        connect()
        """
    elif type == "bind_shell":
        code = """
        # Safe Bind Shell Simulation
        import socket
        def start():
            print('[SIMULATION] Starting fake shell listener...')
        start()
        """
    else:
        code = "print('[!] Unknown payload type')"

    encoded = base64.b64encode(code.encode()).decode()
    print(f"[+] Payload (base64 encoded):\n{encoded}")
    return encoded

def save_payload(encoded_payload, filename="safe_payload.py"):
    """
    Writes the simulated payload to a file.
    """
    print(f"[+] Writing payload to {filename}")
    decoded = base64.b64decode(encoded_payload.encode()).decode()
    with open(filename, 'w') as f:
        f.write(decoded)
    print("[+] Payload saved (simulation only).")

if __name__ == "__main__":
    print("=== Payload Laboratory ===")
    print("Select Payload Type:")
    print("1. Reverse Shell (Safe Sim)")
    print("2. Bind Shell (Safe Sim)")
    choice = input("Enter choice: ")

    if choice == '1':
        payload = generate_safe_payload("reverse_shell")
        save_payload(payload, "reverse_sim_payload.py")
    elif choice == '2':
        payload = generate_safe_payload("bind_shell")
        save_payload(payload, "bind_sim_payload.py")
    else:
        print("[!] Invalid choice")
