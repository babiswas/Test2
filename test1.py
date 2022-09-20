import time
def knapsack(arr,val,W,n):
    if n==0 or W==0:
        return 0
    else:
        if n-1>=0:
            if arr[n-1]<=W:
                return max(knapsack(arr,val,W,n-1),knapsack(arr,val,W-arr[n-1],n-1)+val[n-1])
            else:
                return knapsack(arr,val,W,n-1)
            
def knapsack1(arr,val,W,n):
    M=[[-1 for i in range(W+1)] for j in range(n+1)]
    def knapsack_util(arr,val,W,n,M):
        if n==0 or W==0:
            return 0
        else:
            if n-1>=0:
                if arr[n-1]<=W:
                    if M[n][W]!=-1:
                        return M[n][W]
                    else:
                        M[n][W]=max(knapsack_util(arr,val,W,n-1,M),knapsack_util(arr,val,W-arr[n-1],n-1,M)+val[n-1])
                        return M[n][W]
                else:
                    M[n][W]=knapsack_util(arr,val,W,n-1,M)
                    return M[n][W]
    return knapsack_util(arr,val,W,n,M)

if __name__=="__main__":
    print("The knapsack of the array is:")
    t1=time.time()
    print(knapsack([10, 20, 30],[60, 100, 120],50,3))
    print(time.time()-t1)
    print("The knapsack of the array is:")
    t2=time.time()
    print(knapsack1([10, 20, 30],[60, 100, 120],50,3))
    print(time.time()-t2)
    
          
          