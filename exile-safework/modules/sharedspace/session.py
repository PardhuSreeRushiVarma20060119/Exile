# session.py - Exile-SafeWork v1.0.4
# Session Tracker for Safe Payload Execution

import uuid
import time
import random

sessions = {}

class Session:
    def __init__(self, type="reverse_shell"):
        self.session_id = str(uuid.uuid4())[:8]
        self.created_at = time.ctime()
        self.type = type
        self.status = "active"

    def terminate(self):
        self.status = "terminated"
        print(f"[-] Session {self.session_id} terminated.")

    def __str__(self):
        return f"[Session ID: {self.session_id} | Type: {self.type} | Status: {self.status} | Created: {self.created_at}]"

def create_session(type="reverse_shell"):
    s = Session(type)
    sessions[s.session_id] = s
    print(f"[+] New Session Created: {s.session_id}")
    return s.session_id

def list_sessions():
    print("\n[+] Active Sessions:")
    if not sessions:
        print("[!] No active sessions.")
    for sid, s in sessions.items():
        print(s)

def terminate_session(sid):
    if sid in sessions:
        sessions[sid].terminate()
    else:
        print("[!] Session ID not found.")

if __name__ == "__main__":
    print("=== Exile SafeWork: Session Tracker ===")
    while True:
        print("\n1. Create New Session")
        print("2. List Sessions")
        print("3. Terminate Session")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            typ = input("Enter session type (reverse_shell/bind_shell/etc): ")
            create_session(typ)
        elif choice == '2':
            list_sessions()
        elif choice == '3':
            sid = input("Enter session ID to terminate: ")
            terminate_session(sid)
        elif choice == '4':
            break
        else:
            print("[!] Invalid option")
