class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = slow = fast = ListNode(-math.inf)
        dummy.next = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next # 이 부분이 삭제를 담당함
        return dummy.next

        