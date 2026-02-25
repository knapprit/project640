print("Поточное XOR-шифрование")

text = input("Введите текст: ")
key = int(input("Введите ключ (1-255): "))

result = ""

for symbol in text:
    #символ в число
    code = ord(symbol)
    #XOR с ключом
    encrypted_code = code ^ key
    #обратно в символ
    result += chr(encrypted_code)

#вывод в HEX
print("Зашифрованное сообщение (HEX):")
print(result.encode("utf-8").hex())
