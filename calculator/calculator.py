def main():
    while True:
        inp = input()
        if not inp:
            continue
        if inp == '/exit':
            print("Bye!")
            break
        elif inp == "/help":
            print("The program calculates the sum of numbers.")
            continue
        elif inp[0] == "/":
            print("Unknown command")
            continue
        try:
            print(eval(inp))
        except (SyntaxError, NameError):
            print("Invalid expression")


if __name__ == "__main__":
    main()
