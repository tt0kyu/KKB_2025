from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import binascii


def decrypt(data, key):
    cipher = AESGCM(key)
    nonce = data[:12]
    ciphertext = data[12:]
    plaintext = cipher.decrypt(nonce, ciphertext, None)
    return plaintext


target_file = "flag.txt.ryk"
output_file = "flag.txt"
hex_key = "133a985d25765d4af3c84fcb1f8296f888d5d8fa028697e186939dbaf283108e"

try:
    aes_key = binascii.unhexlify(hex_key)

    with open(target_file, "rb") as f:
        ciphertext_blob = f.read()

    plaintext = decrypt(ciphertext_blob, aes_key)

    print("복호화 성공!")
    print("\n--- FLAG ---")
    print(plaintext.decode('utf-8'))

    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"\n 평문 저장'{output_file}'")

except Exception as e:
    print(f"오류 발생: {e}")