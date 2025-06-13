# vault.py - Exile-SafeWork v1.0.4
# Secure Storage Emulator for Simulated Payloads, Stagers, Configs

import os
import json
import uuid
import time

class Vault:
    def __init__(self, vault_path="exile_vault"):
        self.vault_path = vault_path
        if not os.path.exists(self.vault_path):
            os.makedirs(self.vault_path)

    def store_item(self, name, content):
        file_id = str(uuid.uuid4())[:8]
        filename = f"{file_id}_{name}.json"
        filepath = os.path.join(self.vault_path, filename)
        with open(filepath, 'w') as f:
            json.dump({"timestamp": time.ctime(), "name": name, "content": content}, f, indent=4)
        print(f"[+] Stored '{name}' as {filename}")

    def list_items(self):
        files = os.listdir(self.vault_path)
        if not files:
            print("[!] Vault is empty.")
            return
        print("\n=== Vault Contents ===")
        for f in files:
            print(f" - {f}")

    def retrieve_item(self, filename):
        filepath = os.path.join(self.vault_path, filename)
        if not os.path.exists(filepath):
            print("[!] File not found in vault.")
            return
        with open(filepath, 'r') as f:
            data = json.load(f)
            print(f"\n[Retrieved: {filename}]\nName: {data['name']}\nStored: {data['timestamp']}\nContent:\n{data['content']}")

if __name__ == "__main__":
    print("=== Exile SafeWork: Vault Emulator ===")
    vault = Vault()
    while True:
        print("\n1. Store Item")
        print("2. List Vault Items")
        print("3. Retrieve Item")
        print("4. Exit")
        choice = input("Select option: ")
        if choice == '1':
            name = input("Item name: ")
            content = input("Item content: ")
            vault.store_item(name, content)
        elif choice == '2':
            vault.list_items()
        elif choice == '3':
            fname = input("Filename to retrieve: ")
            vault.retrieve_item(fname)
        elif choice == '4':
            break
        else:
            print("[!] Invalid choice.")
