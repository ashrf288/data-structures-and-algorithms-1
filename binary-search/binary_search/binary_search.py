def  binary_search (array,key):
  low=0
  high=len(array)-1

  while low<=high:
      mid=(low+high)//2

      if key==array[mid]:
          return mid
      elif key<array[mid]:
          high=mid-1
      else :
          return -1
