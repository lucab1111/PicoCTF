import sys


def dec(flag):
    print(
        "".join(
            [
                # chr(
                chr(int(flag[i : i + 16], 2))
                # )
                # "" + str(i)
                for i in range(0, len(flag), 16)
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
        #     "If not a multiple of 16, rightmost bits will be padded e.g. 11111111111111111 -> 111111111111111100000001"
        # )
        enc(sys.argv[1])
# cat enc | xargs python3 encDecoder.py
