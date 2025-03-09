#merge two lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
from typing import Optional
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy=ListNode(-1)
        current=dummy
        while(list1 and list2): #comparing what is happeing 
           if(list1.val > list2.val):
              current.next=list2
              list2=list2.next
           else:
               current.next=list1
               list1=list1.next
           current=current.next
        #when one of the list is ended
        if list1:
            current.next = list1
        else:
            current.next = list2
        current=dummy.next 
        while(current):
            print(current.val, end=" -> " if current.next else "\n")  
            current = current.next
        
           

# Create a linked list:
#list 1 : 1->3->4
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
#list 2 : 1->2->5
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(5)
sol=Solution()
print(sol.mergeTwoLists(head,head1))