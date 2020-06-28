'''
@Author: Zikuan Wang
@Date: 2020-05-08 18:06:26
@LastEditTime: 2020-05-09 00:49:57
@LastEditors: Please set LastEditors
@Description: 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
@FilePath: \python_code\leetcode\addtwonumbers.py
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
# 便于打印输出查看(__str__是python的内置函数，在调用print或者str函数是生效，其效果是把结果转化为字符串输出) 
    def __str__(self): 
        node = self
        lst = []
        while node:
            lst.append(str(node.val))
            node = node.next
        return " -> ".join(lst)

# 自定义的'链表类' (便于生成测试案例)
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, e):
        e = ListNode(e)
        # 先让传入的新节点接手'head后的节点', 再让'head'接手这个新节点 (不会导致引用丢失) 逆序储存
        e.next = self.head
        self.head = e
        return self

    # 便于打印输出查看
    def __str__(self):
        node = self.head
        lst = []
        while node:
            lst.append(str(node.val))
            node = node.next
        return " -> ".join(lst)

class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 排除l1和l2的特殊情况
        if l1 is None and l2 is None:
            return None
        carry_bit = 0 # 保留'进位数' (用于叠加计算)
        # 哑节点的作用: 存储真正的'头部' (当然用其他随便什么变量存都行, 只是一个通用的叫法)
        dummy_node = tail_node = ListNode(0)  # 哑节点和尾节点 都先默认指向一个空节点
        while l1 or l2 or carry_bit:
            l1_val = l1.val if l1 else 0 # 如果这个节点已经移到None了, 把它的值视为:0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry_bit # 每次计算要加上'上次计算的进位数'
            carry_bit = sum // 10
            tail_node.next = ListNode(sum % 10)  # 先把新传入的节点作为'尾节点'的后一个节点
            tail_node = tail_node.next # 再把尾节点后移到'尾部'
            l1 = l1.next if l1 else None # 若l1和l2不为None,都向后移动
            l2 = l2.next if l2 else None
        return dummy_node.next # 代表真正的'头部'节点



if __name__ == "__main__":
# 用自己定义的'链表'类, 生成两串题目要求的 l1和l2
    linked_lst1 = LinkedList()
    linked_lst1.add(3).add(4).add(2)
    l1=linked_lst1.head

    linked_lst2 = LinkedList()
    linked_lst2.add(4).add(6).add(5)
    l2 = linked_lst2.head

# 测试
    res = Solution().addTwoNumbers(l1, l2)
    print(l1)
    print(l2)
    print(res)
    
