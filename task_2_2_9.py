from simplecrypt import decrypt, DecryptionException

encrypted = open("encrypted.bin", "rb").read()
with open("passwords.txt") as passwords:
    for password in passwords.read().splitlines():
        print(password)
        try:
            decrypted = decrypt(password, encrypted)
            print(decrypted)
            break
        except DecryptionException:
            pass



