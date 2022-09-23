def subset_sum(arr,W,n):
    if W==0:
        return True
    elif n==0:
        return False
    else:
        if n-1>=0:
            if arr[n-1]<=W:
                return subset_sum(arr,W,n-1) or subset_sum(arr,W-arr[n-1],n-1)
            else:
                return subset_sum(arr,W,n-1)
            
def subset_sum2(arr,W,n):
    M=[[False for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0:
                M[i][j]=False
            if j==0:
                M[i][j]=True
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=j:
                    M[i][j]=M[i-1][j] or M[i-1][j-arr[i-1]]
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]
                
            
if __name__=="__main__":
    print(subset_sum([2,3,7,8,10],11,5))
    print(subset_sum2([2,3,7,8,10],11,5))
    
        