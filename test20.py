import sys
#kadanes algorithm
def kadanes_algorithm(arr,n):
    maxm=-sys.maxsize+1
    current=0
    start_index=-1
    end_index=0
    for i in range(n):
        if start_index==-1:
            start_index=i
        current+=arr[i]
        if current>maxm:
            maxm=current
            end_index=i
        if current<0:
            current=0
            start_index=-1
    return start_index,end_index

if __name__=="__main__":
    l=[2,-3,4,-1,-2,1,5,3]
    start_index,end_index=kadanes_algorithm(l,8)
    print(sum(l[start_index:end_index+1]))