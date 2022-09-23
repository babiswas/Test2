def find_lcs(arr,brr,m,n):
    M=[[-1 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                M[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr[i-1]==brr[j-1]:
                M[i][j]=1+M[i-1][j-1]
            else:
                M[i][j]=max(M[i-1][j],M[i][j-1])
    return M

def print_sequence(arr,brr,m,n):
    M=find_lcs(arr,brr,m,n)
    index1=m
    index2=n
    str1=''
    while index1>0 and index2>0:
        if arr[index1-1]==brr[index2-1]:
            str1+=arr[index1-1]
            index1-=1
            index2-=1
        else:
             if M[index1-1][index2]>M[index1][index2-1]:
                index1-=1
             else:
                index2-=1
    return str1[::-1]

if __name__=="__main__":
    print(print_sequence("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB")))