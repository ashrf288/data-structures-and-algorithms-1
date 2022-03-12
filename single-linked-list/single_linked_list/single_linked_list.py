 

class Node : 
    """ Node class has 2 properties:
     1-  the value stored in the Node.
     2-  a pointer to the next Node.
    """
    def __init__(self,value):
        self.value=value
        self.next=None
    
    def __str__(self):
        return f"{self.value},the  next node={self.next} "

    
class Linked_List:
    """
    Linked List class include a head property.
    This class contain the following methods : insert ,includes,to string

    """

    def __init__(self):
        """
        the initial state of head is None 
        , because we initialize LS FROM SCRATCH 

        """
        self.head=None

    def insert(self,value):
        """
        it recives value in the Arguments and  Returns: nothing
        this method Adds a new node with that value to the head of the list 
        with an O(1) Time performance.

        """

        #1-if there is no head we need to add head firstly 
        try :
            new_node=Node(value)
            new_node.next=self.head  
            self.head=new_node     
            
        except:
            return " an error happend when i try to use the insert method "


    def includes(self,value):
        """
        Arguments: value
        Returns: Boolean
        this method traverse the array to  indicates whether 
        a specific value exists as a Nodes value somewhere within the list.
        """
        current=self.head # the first node 
        try:
            while current:
                if current.value==value:
                  return True
                else:
                  current=current.next
            return False # in case it dose NOT find the value after traversing the list 
        except:
            print("an error happend when i try to use the includes method ")

    def to_string(self):
        """
        Arguments: none
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """

        result=''
        current=self.head


        while True:
                if current!=None:
                    result +='{ '+str(current.value)+' } -> '
                    current=current.next
                elif current==None:
                    result+= 'NULL'
                    break
        return result
        

         
 ############################################         
if __name__=="__main__":
    ll=Linked_List()
    print(ll.head)#==>none
    ll.insert("elyas")
    ll.insert("eman")
    ll.insert("nuha")
    print(ll.head.value)
    print(ll.head.next.value)
    print (ll.to_string())




  






  

