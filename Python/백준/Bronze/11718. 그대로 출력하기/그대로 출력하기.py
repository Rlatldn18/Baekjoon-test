while True:
    try:
        str_ = input()
        print(str_)
    except EOFError:
        break