def find_minm_trains(arr,dep):
    count=0
    dep.sort()
    arr.sort()
    needed_platform=0
    pointer1=0
    pointer2=0
    for i in range(len(arr)):
        if arr[pointer1]<dep[pointer2]:
                needed_platform+=1
                pointer1+=1
        elif arr[pointer1]>dep[pointer2]:
            pointer2+=1
            pointer1+=1
    return needed_platform
    
if __name__=="__main__":
    print(find_minm_trains([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]))
    
            
    