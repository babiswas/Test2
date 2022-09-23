def coin_change(C,S,n):
    if n==0 and S!=0:
        return 0
    elif S==0:
        return 1
    else:
        if n-1>=0:
            if C[n-1]<=S:
                return coin_change(C,S,n-1)+coin_change(C,S-C[n-1],n)
            else:
                return coin_change(C,S,n-1)
            
def coin_changes(C,S,n):
    M=[[-1 for i in range(S+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(S+1):
            if i==0 and j!=0:
                M[i][j]=0
            elif j==0:
                M[i][j]=1
    for i in range(n+1):
        for j in range(S+1):
            if i-1>=0:
                if C[i-1]<=j:
                    M[i][j]=M[i-1][j]+M[i][j-C[i-1]]
                else:
                    M[i][j]=M[i-1][j]
    return M[n][S]
            
if __name__=="__main__":
    print(coin_change([2, 5, 3, 6],10,4))
    print(coin_changes([2, 5, 3, 6],10,4))
    