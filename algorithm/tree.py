# -*- coding: UTF-8 -*-
"""
实现二叉树基础数据结构和三种遍历方式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class TreeNode(object):

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


class Tree(object):

    def __init__(self, root_node):
        self.root_node = root_node

    def dlr_order(self):
        """ 前序遍历二叉树
        """
        d = self.root_node
        print d.root

        l = d.left
        r = d.right

        for node in [l, r]:
            if node:
                Tree(node).dlr_order()

    def ldr_order(self):
        """ 中序遍历二叉树
        """
        d = self.root_node
        l = d.left
        r = d.right
        if l:
            Tree(l).ldr_order()
        print d.root
        if r:
            Tree(r).ldr_order()

    def lrd_order(self):
        """ 后序遍历二叉树
        """
        d = self.root_node
        l = d.left
        r = d.right
        if l:
            Tree(l).lrd_order()
        if r:
            Tree(r).lrd_order()
        print d.root


if __name__ == "__main__":
    node4 = TreeNode(4)
    node3 = TreeNode(3)

    node1 = TreeNode(1, node3, node4)
    node2 = TreeNode(2)
    node0 = TreeNode(0, node1, node2)

    # 遍历二叉树
    tree = Tree(node0)

    print 'dlr order'
    tree.dlr_order()

    print 'ldr order'
    tree.ldr_order()

    print 'lrd order'
    tree.lrd_order()
