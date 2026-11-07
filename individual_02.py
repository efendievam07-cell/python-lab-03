def main() -> None:
    word = input("Введите слово: ")

    if word == word[::-1]:
        print("Да")
    else:
        print("Нет")


if __name__ == "__main__":
    main()