import sys

def solve()->None:

    data = sys.stdin.read().splitlines()

    s = data[0]

    p = data[1]

    ns = len(s)

    np = len(p)

    need = [0 for _ in range(26)]

    windows = [0 for _ in range(26)]

    ans = []

    for i in range(np):

        need[ord(p[i])-ord("a")]+=1
        windows[ord(s[i])-ord("a")]+=1

    if need==windows:
        ans.append(0)


    for i in range(np,ns,1):

        windows[ord(s[i])-ord("a")]+=1

        windows[ord(s[i-np])-ord("a")]-=1

        if windows==need:
            ans.append(i-np+1)

    n_ans = len(ans)

    print(n_ans)

    if n_ans>0:

        print(*ans)




if __name__ =="__main__":
    solve()