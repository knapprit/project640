def decrypt_caesar(text, key):
    key = key % 26
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            result += ch

    return result


cipher = input("Введите шифртекст: ")
key = int(input("Введите ключ: "))

plain = decrypt_caesar(cipher, key)
print("Открытый текст:", plain)
