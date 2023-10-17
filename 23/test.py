from solution import ListNode, Solution

result = Solution().mergeKLists(
    [
        ListNode( 1, ListNode(4, ListNode(5)) ),
        ListNode( 1, ListNode(3, ListNode(4)) ),
        ListNode( 2, ListNode(6))
    ])

result.print()
