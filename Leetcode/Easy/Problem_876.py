# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
#we are also trying to flyod -cycle alogthirm fast and slow and it will help us in my problems 
from typing import Optional
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #soultion 1 
    # def hasCycle(self, head: Optional[ListNode]) -> bool: 
    #     slow=head
    #     fast=head
    #     count=0
    #     while(fast):
    #         count+=1
    #         fast=fast.next
    #     middle= math.ceil(count/2)
    #     count=0
    #     while(slow and count<middle):
    #         count+=1
    #         slow=slow.next
    #     while(slow):
    #         print(f"{slow.val} ->", end="")
    #         slow=slow.next
        


    #soultion 2
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow.val   

# Create a linked list: 10 -> 15 -> 4 -> 20 -> 12
head = ListNode(10)
head.next = ListNode(15)
head.next.next = ListNode(4)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(12)
sol=Solution()
print(sol.middleNode(head))