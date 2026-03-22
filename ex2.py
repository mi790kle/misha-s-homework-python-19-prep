secret_code: list[int] = [77, 12, 43, 100, 51]
def entrance_with_secret_code(secret_code: list[int]) -> None:
    index: int = 0
    while True:
        num = input("Enter a number: ")
        if not num.strip().isdigit():
            print("NUMBER please")
            continue
        num = int(num.strip())
        if num == secret_code[index]:
            print("Correct!")
            index += 1
            if index == len(secret_code):
                print("You're in!")
                break
            else:
                continue
        else:
            print("Wrong number! Restarting...")
            index = 0
            continue
entrance_with_secret_code(secret_code)