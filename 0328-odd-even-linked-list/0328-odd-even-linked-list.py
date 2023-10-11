# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd_dummy = odd = ListNode(-math.inf)
        even_dummy = even = ListNode(-math.inf)

        index = 1

        while head:
            if index % 2 == 1: # 홀수 노드
                odd.next = head
                odd = odd.next # 홀수 노드를 연결
            else: # 짝수 노드
                even.next = head 
                even = even.next # 짝수 노드를 연결
        
            head = head.next
            index += 1
        
        odd.next = even_dummy.next # 홀수번째의 끝을 짝수번째의 처음에 연결
        even.next = None # 짝수번째의 끝을 None으로 지정

        return odd_dummy.next





        