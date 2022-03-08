def binary_search(array, value):
    """
     function called BinarySearch which 
     takes in 2 parameters: a sorted array and the search key. 
     return the index of the arrays element that is equal to the value of the search key, 
     or -1 if the element is not in the array.
    """


    low = 0
    high = len(array)

    while low <= high:
       mid = (low+high)//2
     
       if array[mid] ==value :
        return mid
       elif array[mid] <value :
         low=mid+1
       elif array[mid] >value :
         high=mid-1
       else:
         return -1
    return array
