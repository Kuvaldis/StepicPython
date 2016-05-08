def step7():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        if re.match(r".*cat.*cat.*", line):
            print(line)


def step8():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        if re.match(r".*\bcat\b.*", line):
            print(line)


def step9():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        if re.match(r".*z...z.*", line):
            print(line)


def step10():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        if re.match(r".*\\.*", line):
            print(line)


def step11():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        if re.match(r".*\b(\w+)\1\b", line):
            print(line)


def step12():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        print(line.replace("human", "computer"))


def step13():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        print(re.sub(r"\b[a]+\b", "argh", line, 1, re.IGNORECASE))


def step14():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        print(re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line))


def step15():
    import sys
    import re
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        print(re.sub(r"(\w)(\1*)", r"\1", line))


# def step16(line):
#     import sys
#     import re
#     if not re.fullmatch(
#             r"(([0]{1,4}|[0]{0,2}11|[0]?110|1001|1100|1111)"
#             r"(0000|0011|0110|1001|1100|1111)*)|"
#             r"(([0]{0,2}10|[0]?101|1000|1011|1110)(0001|0100|0111|1010|1101)"
#             r"((0001|0100|0111|1010|1101)*(0010|0101|1000|1011|1110)*)*)|"
#             r"(([0]{0,3}1|[0]?100|[0]?111|1010|1101)(0010|0101|1000|1011|1110)"
#             r"((0001|0100|0111|1010|1101)*(0010|0101|1000|1011|1110)*)*)",
#             line):
#         print(line)
#
#
# for i in range(0, 1024, 3):
#     step16(format(i, "#010b").lstrip('0').lstrip('b'))
