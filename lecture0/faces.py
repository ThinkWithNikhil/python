def main():
    user_input = str(input("Input: "))
    print(convert(user_input))

def convert(user_input: str):
    return user_input.replace(":)", "🙂").replace(":(", "🙁")

main()