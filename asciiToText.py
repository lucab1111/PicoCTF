import sys


def asciiToText(arg):
    text = ""
    f = open(arg, "r")
    for line in f.readlines():
        text += chr(int(line))
    return text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 argument needed only")
    else:
        print(asciiToText(sys.argv[1]))
