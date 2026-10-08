import sys

def solve()->None:

    s = input()

    n = len(s)

    dp = [[False] * n for _ in range(n)]

    

    best_lenth = 0

    best_index = n

    for i in range(n-1,-1,-1):
        for j in range(i,n,1):
                
            if j-i<=1:
                dp[i][j]=True if s[j]==s[i] else False
                
            else:
                dp[i][j]= s[j]==s[i] and dp[i+1][j-1]


            if dp[i][j]:

                if (j-i+1)>=best_lenth:

                    best_lenth = j-i+1 
                    best_index = i
            


    print(s[best_index:best_index+best_lenth])
            
        











if __name__ == "__main__":
    solve()