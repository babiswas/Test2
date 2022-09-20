import sys
def subarray(arr,n):
    max=-sys.maxsize+1
    temp_sum=0
    start_index=0
    end_index=0
    for i in range(n):
        temp_sum+=arr[i]
        if max<temp_sum:
            max=temp_sum
            start_index=i
            end_index=i
        if i+1<n:
            for j in range(i+1,n):
                temp_sum+=arr[j]
                if max<temp_sum:
                    max=temp_sum
                    start_index=i
                    end_index=j
        temp_sum=0
    return start_index,end_index

def kadanes_algo(arr,n):
    max=-sys.maxsize+1
    current_sum=0
    for i in range(n):
        current_sum+=arr[i]
        if max<current_sum:
            max=current_sum
        if current_sum<0:
            current_sum=0
    return max
        

if __name__=="__main__":
    start_index,end_index=subarray([-2, -3, 4, -1, -2, 1, 5, -3],8)
    print(start_index,end_index)
    print("Maximum sum subarray:")
    print(kadanes_algo([-2, -3, 4, -1, -2, 1, 5, -3],8))
                    
                   
        