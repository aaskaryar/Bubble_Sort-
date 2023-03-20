import time

def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
        print(nlist)
        time.sleep(1)

nlist = [14,46,43,27,57,41,45,21,70]
print("Original list:", nlist)
bubbleSort(nlist)
print("Sorted list:", nlist)
