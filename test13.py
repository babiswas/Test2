def subset_sum(arr,W,n):
    M=[[False for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 and j!=0:
                M[i][j]=False
            if j==0:
                M[i][j]=True
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if arr[i-1]<=W:
                    M[i][j]=M[i-1][j] or M[i-1][j-arr[i-1]]
                else:
                    M[i][j]=M[i-1][j]
    return M


def minimum_subset_diff(arr,W,n):
    sm=sum(arr)
    maxm=0
    M=subset_sum(arr,W,n)
    for i in range((sm//2)+1):
        if M[n][i]==True:
            if i>maxm:
                maxm=i
    return sm-2*maxm
              

if __name__=="__main__":
    print(minimum_subset_diff([1,2,7],10,3))
    
    