print("Поточное XOR-дешифрование")

cipher_hex = input("Введите HEX: ")
key = int(input("Введите ключ (1-255): "))

#из HEX в обычную строку
cipher_text = bytes.fromhex(cipher_hex).decode("utf-8")

result = ""

for symbol in cipher_text:
    code = ord(symbol)
    decrypted_code = code ^ key
    result += chr(decrypted_code)

print("Расшифрованный текст:")
print(result)
