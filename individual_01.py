def main() -> None:
    sentence = input("Введите предложение: ")
    space_count = sentence.count(" ")
    print(f"Количество пробелов: {space_count}")


if __name__ == "__main__":
    main()