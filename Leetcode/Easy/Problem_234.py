# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Input: head = [1,2,2,1]
# Output: true

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
          slow=head
          fast=head
          while(fast and fast.next): #here we making the slow pointer to middle of the elemnet 
              fast=fast.next.next
              slow=slow.next
          prev,curr=None,slow
          while(curr): #we are trying to reverse the node from middle till end.
              next_node=curr.next #we do this so we don't lose the value 
              curr.next=prev  #now this will be last node as we are reversing so it would be like 2->none 
              prev=curr     #what we do here is here it will come first element after mid which will be 2
              curr=next_node #next the value it will be i mean like it would be 5
          slow=head
          while(prev and slow):
              if(prev.val==slow.val):
                  slow=slow.next
                  prev=prev.next
              else:
                  print("not equal")
                  break
          print("it worked ")
# Create a linked list: 1 ->1-> 2 -> 2 -> 5
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(1)
sol=Solution()
sol.isPalindrome(head)