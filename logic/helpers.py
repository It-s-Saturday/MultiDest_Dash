def stars():
    print("*" * 10)


def debug(*msg):
    print()
    stars()
    for m in msg:
        print(m)
    stars()
    print()
