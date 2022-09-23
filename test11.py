def count_subset(arr,W,n):
    if n==0 and W!=0:
      return 0
    elif W==0:
      return 1
    elif W==0 and n==0:
      return 1
    else:
        if n-1>=0:
            if arr[n-1]<=W:
                return count_subset(arr,W,n-1)+count_subset(arr,W-arr[n-1],n-1)
            else:
                return count_subset(arr,W,n-1)

def count_subsets(arr,W,n):
    M=[[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 and j!=0:
                M[i][j]=0
            elif j==0:
                M[i][j]=1
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=j:
                    M[i][j]=M[i-1][j]+M[i-1][j-arr[i-1]]
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]

if __name__=="__main__":
    print(count_subset([2,3,5,6,8,10],10,6))
    print(count_subsets([2,3,5,6,8,10],10,6))
    
    