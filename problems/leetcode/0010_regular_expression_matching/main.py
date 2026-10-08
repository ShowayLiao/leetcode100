import sys
from functools import lru_cache

def matches(ch:str,x:str)->bool:
    return (
        ch==x
        or x=="."
    )


def solve()->None:

    s = sys.stdin.readline().rstrip("\r\n")
    p = sys.stdin.readline().rstrip("\r\n")

    @lru_cache(maxsize=None)
    def match(i:int,j:int)->bool:
        if j==len(p):
            return i==len(s)

        first_match = (
            i<len(s)
            and matches(s[i],p[j])
        )

        if j+1<len(p) and p[j+1]=="*":
            return(
                match(i,j+2)
                or (first_match and match(i+1,j))
            )

        return (first_match and match(i+1,j+1))

    print("true" if match(0,0) else "false")



if __name__ == "__main__":
    solve()
