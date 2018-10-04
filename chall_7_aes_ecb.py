from Crypto.Cipher import AES
import base64

def aes_ecb(ciphertext,key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


if __name__ == "__main__":
    key = b'YELLOW SUBMARINE'
    with open("7.txt","r") as f:
        ciphertext = "".join(line.strip() for line in f)
    ciphertext = base64.b64decode(ciphertext)
    print aes_ecb(ciphertext,key)

