# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode):
    #     '''
    #     递归，效率更高
    #     '''
    #     if not l1 or not l2:
    #         return l1 or l2
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        '''
        迭代
        '''
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    print(s.mergeTwoLists())