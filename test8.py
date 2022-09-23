def knapsack(arr,brr,W,n):
    M=[[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
               M[i][j]=0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=j:
                    M[i][j]=max(M[i-1][j],M[i-1][j-arr[i-1]]+brr[i-1])
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]

if __name__=="__main__":
    print(knapsack([10, 20, 30],[60, 100, 120],50,3))
    
                