_debug = False


def stars():
    print("*" * 10)


def debug(*msg):
    if _debug:
        print()
        stars()
        for m in msg:
            print(m)
        stars()
        print()
