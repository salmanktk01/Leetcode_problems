#reverse the linked list 

from typing import Optional
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
   def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       current=head
       prev=None
       while current:
           next_node=current.next #this is so we should not lose the value
           current.next=prev  #as it should be last element now 2-> none
           prev=current  #we do this so we can have prev value address and can reverse it prev 2->none and 5 will be added 
           current=next_node  #mean second element in a list 
       while(prev):
            print(prev.val, end=" -> " if prev.next else "\n")  
            prev = prev.next
        
           

# Create a linked list: 10 -> 15 -> 4 -> 20 -> 12
head = ListNode(10)
head.next = ListNode(15)
head.next.next = ListNode(4)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(12)
sol=Solution()
print(sol.reverseList(head))