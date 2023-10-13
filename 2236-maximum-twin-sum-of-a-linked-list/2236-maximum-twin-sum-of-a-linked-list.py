# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        max_sum = float('-inf')

        def reverse(head): # ll을 뒤집는 함수
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev,curr = curr,next_node
            return prev
        
        slow, fast = head, head
        while fast: # slow는 한칸씩, fast는 2칸씩 전진
            slow = slow.next
            fast = fast.next.next
        # slow는 주어진 linked list의 반만 전진 가능 --> 그 반에서 남는 부분이 뒤쪽임
        first = head
        second = reverse(slow) # 남는 부분 뒤쪽을 뒤집음

        while second:
            value = first.val + second.val
            max_sum = max(max_sum, value)
            first = first.next
            second = second.next
        
        return max_sum
        



        
        