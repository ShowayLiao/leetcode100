import sys

def solve()->None:

    x = int(sys.stdin.readline())

    sign = -1 if x<0 else 1

    x = abs(x)

    result = 0

    while x>0:
        digit = x%10
        result = result*10+digit
        x = x//10

    print(sign*result if (-2**31)<=result<(2**31) else 0)


    






if __name__ == "__main__":
    solve()