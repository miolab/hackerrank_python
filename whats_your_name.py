def print_full_name(a, b):
    a, b = str(first_name), str(last_name)
    str_hd = "Hello "
    str_tl = "! You just delved into python."
    print(str_hd + a + " " + b + str_tl)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)