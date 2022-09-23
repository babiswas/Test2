import sys
def min_coins(arr,W,n):
    if W==0:
        return 0
    elif n==0 and W!=0:
        return sys.maxsize-1
    elif W%arr[0]==0:
        return W//arr[0]
    elif W%arr[0]!=0:
        return sys.maxsize-1
    else:
        if n-1>=0:
            if arr[n-1]<=W:
                return min(min_coins(arr,W,n-1),min_coins(arr,W-arr[n-1],n)+1)
            else:
                return min_coins(arr,W,n-1)
            
def minm_coin(arr,W,n):
    M=[[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 and j!=0:
                M[i][j]=sys.maxsize
            elif j==0:
                M[i][j]=0
    for j in range(1,W+1):
        if j%arr[0]==0:
            M[1][j]=j//arr[0]
        else:
            M[1][j]=sys.maxsize-1
    for i in range(2,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=j:
                    M[i][j]=min(M[i-1][j],M[i][j-arr[i-1]]+1)
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]
               
            

            
if __name__=="__main__":
    print(minm_coin([9,6,5,1],11,4))
    print(min_coins([9,6,5,1],11,4))
    
    
            