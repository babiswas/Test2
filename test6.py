def find_pair(arr,target):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j])
                
def sort_pair(arr,target):
    arr.sort()
    low=0
    high=len(arr)-1
    while low<high:
        temp=target-arr[low]
        if temp<arr[high]:
            high=high-1
        elif temp>high:
            low=low+1
        elif temp == arr[high]:
            return arr[low],arr[high]
    return -1

def sort_pairs(arr,target):
    mp=dict()
    for index,value in enumerate(arr):
        mp.update({value:index})
    for index,value in enumerate(arr):
        temp=target-value
        elem=mp.get(temp,-1)
        if elem!=-1 and index!=elem:
            print(temp,value)
    
            
if __name__=="__main__":
    find_pair([0, -1, 2, -3, 1],-2)
    print(sort_pair([0, -1, 2, -3, 1],-2))
    print(sort_pairs([0, -1, 2, -3, 1],-2))
    
        
         
    