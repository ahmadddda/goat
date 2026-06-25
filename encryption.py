import random
import string


def encrypt(message, chars, key):
    # Swap each letter from its position in `chars` to the same position in `key`.
    encrypted = ""
    for letter in message:
        index = chars.index(letter)
        encrypted += key[index]
    return encrypted


def decrypt(message, chars, key):
    # The mirror of encrypt: find the position in `key`, then look up `chars`.
    decrypted = ""
    for letter in message:
        index = key.index(letter)
        decrypted += chars[index]
    return decrypted


def main():
    chars = list(string.punctuation + string.digits + string.ascii_letters)
    # Build the key ONCE so encrypt and decrypt share the exact same shuffled list.
    key = chars.copy()
    random.shuffle(key)

    password = "password"
    encrypted = encrypt(password, chars, key)
    decrypted = decrypt(encrypted, chars, key)

    print("Original: ", password)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()