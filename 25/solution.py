from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:

    @staticmethod
    def swap( self, n:int=-1, length=1, prev=None, new_head=None ):

        """
        Given 
            self: the head node
            n:    the number of nodes to flip and return
        
        Recursively swaps a node chain 
            ----------------------
            n=-1:     1-2-3-4-5 to 5-4-3-2-1
            n= 3:     1-2-3-4-5 to 3-2-1 
            n= 2:     1-2-3-4-5 to 2-1
            ----------------------

        returns 
            new_head: the new head node
            self:     the new tail node (whichever node was first called)
            next:     the next node in the chain (None if you exhausted the whole chain)
            length:   the length of the parsed node chain 
        """

        n = n-1 #prevents unituitive off-by-one swapping
        new_head = self
        next = self.next #keep track of what node is next in line
        
        #has a child or done swapping
        if self.next != None and n != 0:
            new_head, _, next, length = Node.swap( self.next, n, length+1, prev=self, new_head=new_head )

        #swap the prev to be next
        self.next = prev

        #return new_head, new_tail, next item up, and length of the chain
        return new_head, self, next, length #end of recursion
        
    @staticmethod
    def swap_every_k( self, k: int ):

        """
        Given 
            k: integer which decides the break point for the number of ints to flip

        flip the node chain in chunks of nodes with length of k
            ----------------------
            k= 3:     1-2-3-4-5 to 3-2-1-4-5
            k= 2:     1-2-3-4-5 to 2-1-4-3-5
            k= 5:     1-2-3-4-5 to 5-4-3-2-1
            ----------------------
        
        Returns 
            new_head: the head node of the flipped chain
        """

        new_head, new_tail, next, length = Node.swap( self, n=k )
        if length >= k:
            if next != None:
                new_tail.next = Node.swap_every_k( next, k )

        # this is the end of the chain, switch the order back and then return; this is the end of the recursion
        else:
            new_head, new_tail, next, length = Node.swap( new_head )
            return new_head

        return new_head
    
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return Node.swap_every_k( head, k )


