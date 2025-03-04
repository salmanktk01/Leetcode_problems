# Remove Duplicates from Sorted List
# Input: head = [1,1,2]
# Output: [1,2]

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> bool:
          slow=head
          while(slow and slow.next):
               if(slow.val==slow.next.val):
                    slow.next=slow.next.next
               else:
                    slow=slow.next
          temp = head
          while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
# Create a linked list: 1 ->1-> 2 -> 2 -> 5
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(1)
sol=Solution()
sol.deleteDuplicates(head)