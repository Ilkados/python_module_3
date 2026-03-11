import sys


def main() -> None:
    print("=== Command Quest ===")
    args = sys.argv
    total_args = len(args)

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments recived: {total_args - 1}")

        index = 1

        while index < total_args:
            print(f"Argument {index}: {sys.argv[index]}")
            index += 1

        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
