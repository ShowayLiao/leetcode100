import sys

def solve()->None:

    s = sys.stdin.readline().rstrip("\r\n")

    p = sys.stdin.readline().rstrip("\r\n")

    need = [0]*26

    windows = [0]*26

    result = []


    for ch in p:
        need[ord(ch)-ord("a")]+=1

    for i in range(len(p)):
        windows[ord(s[i])-ord("a")]+=1

    if need == windows:
        result.append(0)

    for i in range(len(p),len(s),1):
        windows[ord(s[i])-ord("a")]+=1
        windows[ord(s[i-len(p)]-ord("a"))]-=1

        if need==windows:
            result.append(i-len(p)+1)


    print(len(result))

    if len(result)>0:
        print(*result)


if __name__ =="__main__":
    solve()