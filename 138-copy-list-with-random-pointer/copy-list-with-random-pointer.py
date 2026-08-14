"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        hashmap={}
        curr=head
        while curr!=None:
            hashmap[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr!=None:
            temp=hashmap[curr]
            temp.next=hashmap.get(curr.next)
            temp.random=hashmap.get(curr.random)
            curr=curr.next 
        return hashmap[head]