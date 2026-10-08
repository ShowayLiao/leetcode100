import sys


def solve()->None:
    trans = {
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1
    }

    s = sys.stdin.readline().rstrip("\r\n")
    result = 0

    for i in range(len(s)-1,-1,-1):
        if i<len(s)-1 and trans[s[i]]<trans[s[i+1]]:
             result-=trans[s[i]]
        else:
            result+=trans[s[i]]

    print(result)


if __name__ == "__main__":
    solve()
