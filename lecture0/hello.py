def hello(name):
    print(f"Hello, {name}!")


def main():
    name = input("What is your name? : ").strip().title()
    hello(name)

main()