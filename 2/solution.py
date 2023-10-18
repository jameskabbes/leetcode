#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=False) -> Optional[ListNode]:
        
        done = True
        val = 0

        if l1 != None:
            done = False
            val += l1.val
            l1 = l1.next

        if l2 != None:
            done = False
            val += l2.val
            l2 = l2.next

        if carry:
            done = False
            val += 1

        if val >= 10:
            carry = True
            val -= 10
        else:
            carry = False        

        if done:
            return None

        return ListNode( val, next=self.addTwoNumbers( l1, l2, carry=carry ) )
        
answer = Solution().addTwoNumbers( ListNode( 2, ListNode(4, ListNode(3) ) ), ListNode( 5, ListNode( 6, ListNode ( 4 ) ) ) ) 

while answer != None:
    print (answer.val)
    answer = answer.next
