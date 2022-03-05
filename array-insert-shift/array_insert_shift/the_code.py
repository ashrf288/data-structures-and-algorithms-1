from math import ceil 

def insertShiftArray (array,value):
    """
    the insertShiftArray function takes an array 
    and the value to be added to it . 
    then it returns the new array with the value added into the middle of the array 

    input  : insertShiftArray ([2,4,6,8],20) 
    output : [2,4,20,6,8]
    """
    mid_index=ceil(len(array)/2)
    new_array=[]
    for i in range (0,mid_index):
        new_array.append(array[i])
    new_array.append(value)

    for i in range(mid_index,len(array)):
        new_array.append(array[i])
    return new_array

     
###############################
def removeShiftArray (array):
          """
          the removeShiftArray function :  removes an element from 
          the middle index and shifts other elements in the array 
          to fill the new gap.

          """
          index = (len(array))//2
          newarray=  (array[:index] + array[index+1:])
          return  newarray

if __name__ =="__main__":
    print(insertShiftArray([1,2,3,4,10,70,80,90],50))
    print(removeShiftArray([3,3,4,1,5,55,5]))