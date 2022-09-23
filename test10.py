def eq_partition(arr,W,n):
    M=[[False for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0:
               M[i][j]=True
            elif j==0:
               M[i][j]=False
            
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=j:
                    M[i][j]=M[i-1][j] or M[i-1][j-arr[i-1]]
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]

def equal_partition(arr,W,n):
    sm=sum(arr)
    if sm%2==0:
        return eq_partition(arr,W,n)
    else:
        return False
    
if __name__=="__main__":
    print(equal_partition([1,5,11,5],11,4))
    
                    