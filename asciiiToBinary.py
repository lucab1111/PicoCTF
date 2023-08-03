import sys


def dec(flag):
    print(
        "".join(
            [
                # chr(
                chr(int(flag[i : i + 8], 2))
                # )
                # "" + str(i)
                for i in range(0, len(flag), 8)
            ]
        )
    )


def enc(flag):
    print("".join([bin(ord(flag[i]))[2:].zfill(16) for i in range(0, len(flag))]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 argument needed only")
    else:
        # print(
        #     "If not a multiple of 8, rightmost bits will be padded e.g. 111111111 -> 1111111100000001"
        # )
        enc(sys.argv[1])
# cat enc | xargs python3 encDecoder.py
