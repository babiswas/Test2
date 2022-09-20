def binary_search(arr,low,high,key):
    while low<high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binary_search(arr,low,mid,key)
        elif arr[mid]<key:
            return binary_search(arr,mid,high,key)
        
if __name__=="__main__":
    l=[11,14,15,17,19,21,27]
    print(binary_search(l,0,7,15))
    print(binary_search(l,0,7,19))
    print(binary_search(l,0,7,17))
        