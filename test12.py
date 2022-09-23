def find_minm_platforms(arr,dep):
    arr.sort()
    dep.sort()
    pointer1=0
    pointer2=0
    platform_needed=0
    while pointer1<len(arr) and pointer2<len(arr):
        if arr[pointer1]<dep[pointer2]:
            platform_needed+=1
            pointer1+=1
        else:
            pointer1+=1
            pointer2+=1
    return platform_needed

if __name__=="__main__":
    print(find_minm_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]))
    