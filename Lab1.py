import time
import matplotlib.pyplot as plt
def linearsearch(arr,key):
    #start = time.perf_counter()
    for i in range(len(arr)):
        if arr[i]==key:
            return i
def binarysearch(arr,low,high,key):
    if low<=high:
        mid=(high+low)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binarysearch(arr,low,mid-1,key)
        else:
            return binarysearch(arr,mid+1,high,key)
    else:
        return -1

sizes=[]
times=[]
print("Linear Search")
n=int(input("enter the number of times you want to run: "))
for i in range(0,n):
    m=int(input("enter the number of array elements: "))
    sizes.append(m)
    arr=[]
    for j in range(0,m):
        temp=int(input())
        arr.append(temp)
    key=int(input("enter the key to find: "))
    starttime=time.perf_counter()
    res=linearsearch(arr,key)
    endtime=time.perf_counter()
    finaltime=endtime-starttime
    times.append(finaltime)
    print(res)


plt.plot(sizes, times)
plt.ylabel("time taken")
plt.xlabel("size of arrays")
plt.show()
plt.savefig('linearsearch.png')

sizes2=[]
times2=[]
print("Binary Search")
n2=int(input("enter the number of times you want to run: "))
for i in range(0,n2):
    m2=int(input("enter the number of array elements: "))
    sizes2.append(m2)
    arr2=[]
    for j in range(0,m2):
        temp2=int(input())
        arr2.append(temp2)
    key2=int(input("enter the key to find: "))
    starttime2=time.perf_counter()
    res2=binarysearch(arr2,0,m2-1,key2)
    endtime2=time.perf_counter()
    finaltime2=endtime2-starttime2
    times2.append(finaltime2)
    print(res2)

plt.plot(sizes2, times2)
plt.ylabel("time taken")
plt.xlabel("size of arrays")
plt.show()
plt.savefig('binarysearch.png')