def number2letter(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[n]

def main():
    for i in range(0,26):
        print(number2letter(i))

main()