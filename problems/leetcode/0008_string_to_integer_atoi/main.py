import sys

def solve()->None:
    
    s = sys.stdin.readline().strip()

    if not s:
        print(0)
        return
    
    sign = 1
    index = 0
    if s[index] in "+-":
        sign = -1 if s[index] in "-" else sign
        index +=1

    result = 0
    while index<len(s) and "0"<=s[index]<="9":

        result = result*10+ int(s[index])
        index+=1


    print(min(2147483647,result*sign) if sign>0 else max(-2147483648,result*sign))



    


if __name__ == "__main__":
    solve()

