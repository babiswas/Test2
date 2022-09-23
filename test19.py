def longest_substr(arr,brr,m,n):
    count=0
    M=[[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                M[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr[i-1]==brr[j-1]:
                 M[i][j]=1+M[i-1][j-1]
                 if count<M[i][j]:
                    count=M[i][j]
            else:
                M[i][j]=0
    return count
    
        
if __name__=="__main__":
    print(longest_substr("GeeksforGeeks","GeeksQuiz",len("GeeksforGeeks"),len("GeeksQuiz")))
    