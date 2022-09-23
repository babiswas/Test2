def count_subset_sum(arr,W,n):
    M=[[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 and j!=0:
                M[i][j]=0
            if j==0:
                M[i][j]=1
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=j:
                    M[i][j]=M[i-1][j]+M[i-1][j-arr[i-1]]
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]

def subset_sum_diff(arr,W,n):
    sm=sum(arr)
    const=(sm-W)//2
    return count_subset_sum(arr,const,n)

if __name__=="__main__":
    print("The number of subsets with given difference is:")
    print(subset_sum_diff([5, 2, 6, 4],3,4))