import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = AES.block_size  # 16 bytes

def pad(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def derive_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        data = f.read()

    key = derive_key(password)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data))

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

    print(f"[+] Encrypted: {output_file}")

def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        iv = f.read(BLOCK_SIZE)
        ciphertext = f.read()

    key = derive_key(password)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"[+] Decrypted: {output_file}")

def crypter_menu():
    print("\n=== EXILE CRYPTER ===")
    print("[1] Encrypt File")
    print("[2] Decrypt File")
    print("[0] Back to Main Menu")

    choice = input(">> ")

    if choice == "1":
        in_file = input("Input file to encrypt: ")
        out_file = input("Output encrypted file: ")
        password = input("Password: ")
        encrypt_file(in_file, out_file, password)

    elif choice == "2":
        in_file = input("Encrypted file to decrypt: ")
        out_file = input("Output decrypted file: ")
        password = input("Password: ")
        decrypt_file(in_file, out_file, password)

    elif choice == "0":
        return

    else:
        print("[!] Invalid Option")
