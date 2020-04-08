# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def hasCycle(self, head: ListNode):
    #     '''
    #     利用哈希表记录访问过的节点
    #     '''
    #     dic = {}
    #     while head:
    #         if dic.get(head,0) != 0: # 如果不在dic中则返回默认值0
    #             return True
    #         else:
    #             dic[head] = 1
    #         head = head.next
    #     return False

    def hasCycle(self, head: ListNode):
        '''
        快慢指针
        '''
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.reverseList())