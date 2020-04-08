# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode):
        '''
        先添加一个空头，再交换，循环解法
        '''
        # thead = ListNode(-1)
        # thead.next = head
        # c = thead
        # while c.next and c.next.next:
        #     a, b = c.next, c.next.next
        #     c.next, a.next = b, b.next
        #     b.next = a
        #     c = c.next.next
        # return thead.next

    def swapPairs(self, head: ListNode):
        '''
         from pre -> a -> b -> b.next to pre -> b -> a -> b.next
        '''
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


if __name__ == "__main__":
    s = Solution()
    print(s.reverseList())