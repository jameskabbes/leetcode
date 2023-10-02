# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print( self ):
        print ( self.val, end = '' )    
        if self.next != None:
            print ( ' | ', end ='' )
            self.next.print()
        else:
            print ('', end ='\n')    


from typing import Optional, List

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        for list in lists:
            list.print()
        
        return 'solutino'