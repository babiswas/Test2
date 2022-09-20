import sys
def count_majority_element(arr,n):
    majority_element=0
    max=0
    count=0
    for i in range(n):
        count=count+1
        if i+1<n:
            for j in range(i+1,n):
                if arr[j]==arr[i]:
                    count=count+1
                    if count>max:
                        max=count
                        majority_element=arr[i]
            count=0
    return majority_element,max

def count_majority(arr,n):
    max_count=-sys.maxsize
    maj_key=0
    maj_list=dict()
    for i in range(n):
        count=maj_list.get(arr[i],0)
        maj_list.update({arr[i]:count+1})
    for key,value in maj_list.items():
        if value>max_count:
            max_count=value
            maj_key=key
    return maj_key,max_count

def majority_count_sorting(arr,n):
    arr.sort()
    count=0
    element=0
    max_count=-sys.maxsize
    for i in range(n):
        if i-1>=0:
            if arr[i-1]!=arr[i]:
                count=1
                if count>max_count:
                    max_count=count
                    element=arr[i]
            else:
                count=count+1
                if count>max_count:
                    max_count=count
                    element=arr[i]
        else:
            count+=1
            if count>max_count:
                max_count=count
                element=arr[i]
    return element,max_count

def count_majority_element(arr,n):
    count=0
    element=arr[0]
    final_count=0
    for i in range(n):
        if arr[i]==element:
            count=count+1
        else:
            count=count-1
            if count==0:
               element=arr[i]
               count=count+1
    for i in range(n):
        if arr[i]==element:
            final_count+=1
    return element,final_count


if __name__=="__main__":
    print("Find the majority element:")
    print(count_majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4],9))
    print("Find the majority element:")
    print(count_majority([3, 3, 4, 2, 4, 4, 2, 4, 4],9))
    print("The majority count of the element:")
    print(majority_count_sorting([3, 3, 4, 2, 4, 4, 2, 4, 4],9))
    print("The majority element of the array is:")
    print(count_majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4],9))
    
        