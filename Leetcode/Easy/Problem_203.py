#remove the linked list element 
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
from typing import Optional
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
   def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       
       while head and head.val == val:
          head = head.next  
       current=head
       while current and current.next:
           if(current.next.val==val):
               current.next=current.next.next
           else:
               current=current.next
       current=head
       while(current):
           print(current.val, end=" -> " if current.next else "\n")  
           current = current.next
        
           

# Create a linked list: 10 -> 15 -> 4 -> 20 -> 12
head = ListNode(6)
head.next = ListNode(6)
head.next.next = ListNode(4)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(6)
sol=Solution()
print(sol.removeElements(head,6))