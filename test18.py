def lcs(arr,brr,m,n):
    if m==0 or n==0:
        return 0
    else:
        if arr[m-1]==brr[n-1]:
            return 1+lcs(arr,brr,m-1,n-1)
        elif arr[m-1]!=brr[n-1]:
            return max(lcs(arr,brr,m-1,n),lcs(arr,brr,m,n-1))
        
def lcs1(arr,brr,m,n):
    M=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                M[i][j]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr[j-1]==brr[i-1]:
                M[i][j]=1+M[i-1][j-1]
            else:
                M[i][j]=max(M[i][j-1],M[i-1][j])
    return M[n][m]
    
        
if __name__=="__main__":
    print(lcs("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB")))
    print(lcs1("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB")))