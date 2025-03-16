import base64
import os
import string
import random

def generate_random_key(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def xor_encrypt(plain_text, key):
    key_bytes = key.encode("utf-8")
    key_len = len(key_bytes)

    encrypted_bytes = bytearray()
    for i, char in enumerate(plain_text.encode("utf-8")):
        encrypted_byte = char ^ (key_bytes[i % key_len] + i % 20)
        encrypted_bytes.append(encrypted_byte)

    return base64.b64encode(encrypted_bytes).decode("utf-8")

xor_key = generate_random_key(16)
encoded_xor_key = base64.b64encode(xor_key.encode("utf-8")).decode("utf-8")

with open("csharpcode.txt", "r", encoding="utf-8") as file:
        plain_text = file.read()

        systemdll = xor_encrypt("System.dll", xor_key)
        systemcoredll = xor_encrypt("System.Core.dll", xor_key)
        LoadApiName = xor_encrypt("LoadApiName", xor_key)
        ReloadPick = xor_encrypt("ReloadPick", xor_key)
        encrypted_text = xor_encrypt(plain_text, xor_key)

try:
    with open("encrypted.txt", "w", encoding="utf-8") as enc_file:
        enc_file.write(encrypted_text)

    with open("xor_key.txt", "w", encoding="utf-8") as key_file:
        key_file.write(encoded_xor_key)
    with open("systemdll.txt", "w", encoding="utf-8") as key_file:
        key_file.write(systemdll)
    with open("systemcoredll.txt", "w", encoding="utf-8") as key_file:
        key_file.write(systemcoredll)
    with open("loadapi.txt", "w", encoding="utf-8") as key_file:
        key_file.write(LoadApiName)
    with open("ReloadPick.txt", "w", encoding="utf-8") as key_file:
        key_file.write(ReloadPick)

    print(f"✅ Encrypt Completed!\n🔒 'encrypted.txt' created: {encrypted_text}")
    print(f"🔑 'xor_key.txt' created: {encoded_xor_key}")

except Exception as e:
    print(f"❌ HATA: Dosya yazılırken bir hata oluştu: {e}")
