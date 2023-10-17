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

        header_vals = {}
        for i in range(len(lists)):
            if lists[i] != None:
                if lists[i].val != None:
                    if lists[i].val not in header_vals:
                        header_vals[ lists[i].val ] = {i}
                    else:
                        header_vals[ lists[i].val ].add(i)

        return self.merge( lists, header_vals )

    def merge( self, lists, header_vals, min_header_val=None ):

        print (header_vals)
        if len(header_vals) == 0:
            return None

        if min_header_val == None:
            min_header_val = min(header_vals)

        list_index = header_vals[ min_header_val ].pop()

        # get the next node in the list
        next = lists[ list_index ].next
        lists[ list_index ] = lists[ list_index ].next
        
        if next != None:
            if next.val not in header_vals:
                header_vals[ next.val ] = { list_index }
            else:
                header_vals[ next.val ].add( list_index )

        # delete the list index from the dict keys if its empty
        next_header_val = None
        if len(header_vals[ min_header_val ]) == 0:
            del header_vals[min_header_val]
        else:
            next_header_val = min_header_val

        return ListNode( val=min_header_val, next=self.merge( lists, header_vals, min_header_val=next_header_val ) )
