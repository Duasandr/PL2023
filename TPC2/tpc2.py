import sys
from adder import Adder


def main():
    text = sys.stdin.read()
    adder = Adder()

    while text:
        text = adder.process_text(text)


if __name__ == "__main__":
    main()
