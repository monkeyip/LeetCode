# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def reverseList(self, head: ListNode):
    #     '''
    #     递归方法
    #     '''
    #     if not head or not head.next:
    #         return head
    #     # 得到尾部节点
    #     p = self.reverseList(head.next)
    #     # 交换当前head 和 head.next
    #     head.next.next = head # 当前节点的下一节点指向当前节点
    #     head.next = None # 拆掉当前节点的next
    #     return p

    def reverseList(self, head: ListNode):
        '''
        循环遍历方法
        '''
        prev = None
        while head:
            curr = head # 当前节点
            head = head.next # 尾部节点
            curr.next = prev # 当前节点的下一节点指向反转后的节点
            prev = curr
        return prev

# https://www.cnblogs.com/tianqizhi/p/9673894.html

if __name__ == "__main__":
    s = Solution()
    print(s.reverseList())