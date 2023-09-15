from solution import Solution, ListNode

def print_node( self ):
    print ( self.val, end = '' )    
    if self.next != None:
        print ( ' | ', end ='' )
        print_node( self.next )
    else:
        print ('', end ='\n')    

        
head = ListNode( 0, ListNode( 1, ListNode( 2, ListNode( 3, ListNode( 4, ListNode( 5, ListNode( 6 ) ) ) ) ) ) )
head = ListNode( 1, ListNode( 2, ListNode( 3, ListNode( 4, ListNode( 5 ) ) ) ) )

#new_head = Solution().reverseKGroup( head, 3 )
#new_head = Solution().reverseKGroup( head, 2 )
new_head = Solution().reverseKGroup( head, 3 )

print_node( new_head )