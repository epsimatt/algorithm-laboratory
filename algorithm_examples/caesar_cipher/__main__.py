# 평문을 암호화하여, 카이사르 단어를 반환한다.
def caesar_cipher(plain_text: str, shift: int) -> str:
    result = ""

    for i in range(len(plain_text)):
        index = ord(plain_text[i]) - ord('A')
        result += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(index + shift) % 26]

    return result


# 평문을 암호화하여, 카이사르 단어를 반환한다.
def caesar_cipher_idx1(plain_text: str, shift: int) -> str:
    result = ""

    for i in range(len(plain_text)):
        index = ord(plain_text[i]) - ord('A') + 1 # 1 <= index <= 26
        result += " ABCDEFGHIJKLMNOPQRSTUVWXYZ"[((index + (shift - 1)) % 26) + 1]

    return result


# 카이사르 단어를 복호화하여, 평문을 반환한다.
def caesar_decipher(cipher_text: str, shift: int) -> str:
    result = ""

    for i in range(len(cipher_text)):
        index = ord(cipher_text[i]) - ord('A')
        result += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(index - shift) % 26]

    return result


# 카이사르 단어를 복호화하여, 평문을 반환한다.
def caesar_decipher_idx1(cipher_text: str, shift: int) -> str:
    result = ""

    for i in range(len(cipher_text)):
        index = ord(cipher_text[i]) - ord('A') + 1 # 1 <= index <= 26
        result += " ABCDEFGHIJKLMNOPQRSTUVWXYZ"[((index - (shift + 1)) % 26) + 1]

    return result

if __name__ == '__main__':
    encrypted_message = caesar_cipher('HELLO', 3)
    decrypted_message = caesar_decipher('KHOOR', 3)

    print(f"caesar_cipher(): {encrypted_message}")
    print(f"caesar_decipher(): {decrypted_message}")

    pass