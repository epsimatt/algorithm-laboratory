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
        index = ord(plain_text[i]) - ord('A') + 1

        # 문자열의 index는 1부터 26까지의 값이 되어야 한다.
        # 따라서 이동 거리가 `shift - 1`인 카이사르 단어의 각 문자의 index를 구해 1을 더해야 한다.
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
        index = ord(cipher_text[i]) - ord('A') + 1

        # 문자열의 index는 1부터 26까지의 값이 되어야 한다.
        # 따라서 이동 거리가 `shift + 1`일 때 평문의 각 문자의 index를 구해 1을 더해야 한다.
        result += " ABCDEFGHIJKLMNOPQRSTUVWXYZ"[((index - (shift + 1)) % 26) + 1]

    return result


if __name__ == '__main__':

    assert caesar_cipher('HELLO', 3) == 'KHOOR'
    assert caesar_cipher_idx1('WXYZ', 3) == 'ZABC'

    assert caesar_decipher('KHOOR', 3) == 'HELLO'
    assert caesar_decipher_idx1('ZABC', 3) == 'WXYZ'