def caesar_shift(text: str, k: int) -> str:
    k %= 26
    out=[]
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + k)% 26 + base))
        else:
            out.append(ch)
    return "".join(out)


def caesar_bruteforce(ciphertext: str):
    print("\nВарианты перебора ")
    for k in range(26):
        print(f"{k:2d} -> {caesar_shift(ciphertext, -k)}")


def read_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("введите целое число")

def main():
    while True:
        print("\n===caesar chipher ===")
        print("1) Зашифровать")
        print("2) Расшифровать методом перебора")
        print("0) выход")
        choice = input("выберите пункт: ").strip()

        if choice =="0":
            print("end....")
            break

        elif choice=="1":
            text=input("введите открытый текст: ")
            key=read_int("введите ключ: ")
            print("шифр: ", caesar_shift(text, key))
        
        elif choice=="2":
            chipher=input("введите шифртекст: ")
            caesar_bruteforce(chipher)
        else:
            print("error")
if name=="main":
    main()
