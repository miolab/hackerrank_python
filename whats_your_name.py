def print_full_name(a, b):
    a, b = str(first_name), str(last_name)
    print(f"Hello {a} {b}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)