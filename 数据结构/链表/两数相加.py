# -*- coding = utf-8 -*-
# @Time: 2021/3/1 上午 12:45
class ListNode():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def print(self):
        head=self
        while(head):
            print(head.val,end='-')
            head=head.next
        print()
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val + l2.val)
        cur = head
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            cur.next = ListNode(l1.val + l2.val + cur.val // 10)
            cur.val = cur.val % 10
            cur = cur.next
        if cur.val >= 10:
            cur.next = ListNode(cur.val // 10)
            cur.val = cur.val % 10
        return head
if __name__ == '__main__':
    list=ListNode(0)
    list2=ListNode(4)
    rail=list
    rail2=list2
    for i in range(1,5):
        rail.next=ListNode(i)
        rail2.next=ListNode(4-i)
        rail=rail.next
        rail2=rail2.next
    head=Solution.addTwoNumbers(object,l1=list,l2=list2)
    list.print()
    list2.print()
    head.print()