def main() -> None:
    text = input("Введите строку: ")
    result = text.replace(" ", "")
    print(f"Строка без пробелов: {result}")


if __name__ == "__main__":
    main()