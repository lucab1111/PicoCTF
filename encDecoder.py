import sys


def enc(flag):
    print(
        "".join(
            [
                chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
                for i in range(0, len(flag), 2)
            ]
        )
    )


def dec(flag):
    print(
        "".join(
            [
                chr(ord(flag[i]) // (1 << 8)) + chr(ord(flag[i]) % (1 << 8))
                for i in range(0, len(flag))
            ]
        )
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 argument needed only")
    else:
        dec(sys.argv[1])
# cat enc | xargs python3 encDecoder.py
