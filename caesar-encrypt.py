def encrypt_caesar(text, key):
    key = key % 26
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += chs

    return result


text = input("Введите открытый текст: ")
key = int(input("Введите ключ: "))

cipher = encrypt_caesar(text, key)
print("Шифртекст:", cipher)
