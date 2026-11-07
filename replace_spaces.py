def main() -> None:
    text = input("Введите предложение: ")
    result = text.replace(" ", "_")
    print(f"Предложение после замены: {result}")


if __name__ == "__main__":
    main()