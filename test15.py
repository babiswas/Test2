def cut_rod(l,v,W,n):
    if n==0 or W==0:
        return 0
    else:
        if n-1>=0:
            if l[n-1]<=W:
                return max(cut_rod(l,v,W,n-1),cut_rod(l,v,W-l[n-1],n)+v[n-1])
            else:
                return cut_rod(l,v,W,n-1)
            
def rod_cut(l,v,W,n):
    M=[[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                M[i][j]=0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i-1>=0:
                if l[i-1]<=j:
                    M[i][j]=max(M[i-1][j],M[i][j-l[i-1]]+v[i-1])
                else:
                    M[i][j]=M[i-1][j]
    return M[n][W]

if __name__=="__main__":
    print(cut_rod([1,2,3,4,5,6,7,8],[1, 3, 4, 5, 7, 9, 10, 11],8,8))
    print(rod_cut([1,2,3,4,5,6,7,8],[1, 3, 4, 5, 7, 9, 10, 11],8,8))
    
    