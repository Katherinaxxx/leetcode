'''
Author: Catherine Xiong
Date: 2021-08-30 21:45:54
LastEditTime: 2021-08-30 21:50:46
LastEditors: Catherine Xiong
Description: 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ans = Node(head.val)
        cur = ans
        while head.next:
            cur.next, cur.random = head.next, head.random
            cur = cur.next
        return ans

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_map = {}
        def Clone1(head):
            if not head:
                return None
            node_map[head] = Node(head.val) 
            if head.next:
                node_map[head].next = Clone1(head.next) 
            if head.random in node_map:
                node_map[head].random = node_map[head.random]
            return node_map[head]
        return Clone1(head)
