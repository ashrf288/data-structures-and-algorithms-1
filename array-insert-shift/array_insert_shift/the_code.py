from math import ceil 

def insertShiftArray (array,value):
    mid_index=ceil(len(array)/2)
    new_array=[]
    for i in range (0,mid_index):
        new_array.append(array[i])
    new_array.append(value)

    for i in range(mid_index,len(array)):
        new_array.append(array[i])
    return new_array

if __name__ =="__main__":
    print(insertShiftArray([1,2,3,4,10,70,80,90],50))
