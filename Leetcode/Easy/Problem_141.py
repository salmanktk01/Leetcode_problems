# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by
#  continuously following the next pointer. Internally, 
# pos is used to denote the index of the node that tail's next pointer is connected to.
#  Note that pos is not passed as a parameter.
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#what we need to do is to find the loop if there is it then return -1 else 0


from typing import Optional


# head=[3,2,0,-4] #yeh postion awein de ho hai 
# Definition for singly-linked list.
#we are also trying to flyod -cycle alogthirm fast and slow and it will help us in my problems 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while(fast and fast.next): #means next 2 pointer and next is not null and we can go onwards
            slow=slow.next 
            fast=fast.next.next
            if(slow==fast): #once we get the loop we will start iterating to find that start of loop node by iterating one by one 
                slow=head
                while(fast!=slow):
                    slow=slow.next 
                    fast=fast.next
                print(slow.val)
                return True 
        return False

# Create a linked list: 10 -> 15 -> 4 -> 20
head = ListNode(10)
head.next = ListNode(15)
head.next.next = ListNode(4)
head.next.next.next = ListNode(20)
head.next.next.next.next = head.next #loop is in that 15 place
sol=Solution()
sol.hasCycle(head)