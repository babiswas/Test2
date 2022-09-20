import sys
def kadanes_algo(arr,n):
    curr_sum=0
    max=-sys.maxsize+1
    index=0
    end_index=0
    start_index=0
    for i in range(n):
        if index==-1:
           index=i
        curr_sum+=arr[i]
        if max<curr_sum:
            max=curr_sum
            start_index=index
            end_index=i
        if curr_sum<0:
            curr_sum=0
            index=-1
    return max,start_index,end_index

if __name__=="__main__":
    print(kadanes_algo([-2, -3, 4, -1, -2, 1, 5, -3],8))
    print(kadanes_algo([-10,-11,-17,-4,-5,-34,-9],7))
        