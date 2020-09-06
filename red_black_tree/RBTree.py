from enum import Enum
from typing import Type

class RBTreeColor:
    Red = 1
    Black = 2

class RBTreeNode:
    """Node inside a Red-Black Tree"""
    __slots__ = ['parent', 'left', 'right', 'value', 'color']

    def __init__(self, value, left=None, right=None, is_root=False):
        self.parent = None
        self.left = left
        if left != None:
            left.parent = self
        self.right = right
        if right != None:
            right.parent = self
        self.value = value
        self.color = RBTreeColor.Black if is_root else RBTreeColor.Red

    @property
    def grandparent(self):
        if self.parent != None:
            return self.parent.parent

    @property
    def parent_sibling(self): 
        gp = self.grandparent
        if gp == None:
            return None
        if gp.left == self.parent:
            return gp.right
        elif gp.right == self.parent:
            return gp.left
        return None

    def insert(self, node):
        if node is None:
            print('Cannot insert nothing')
            return
        if node.value is None:
            print('Cannot insert node with None value')

        if node.value < self.value:
            if node.left is not None:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
                reconcile(node)
        else:
            if node.right is not None:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node
                reconcile(node)

def left_left_rotation(node):
    pass

def left_right_rotation(node):
    pass

def right_left_rotation(node):
    pass

def right_right_rotation(node):
    pass

redBlackTreeReconcilliationStrategy  = {
    3: left_left_rotation,
    2: left_right_rotation,
    1: right_left_rotation,
    0: right_right_rotation
}

def reconcile(node: Type[RBTreeNode]):
    """Given a Red-Black Tree node, change the tree-structure so that the Red-Black Tree is well formed"""
    if node is None:
        print('Cannot reconcile an empty node')
    # If the node is the root then it is always black
    if node.parent is None:
        node.color = RBTreeColor.Black
        return
    # If a parent is red and the child is red then changes need to be made
    if node.color == RBTreeColor.Red and node.parent.color == RBTreeColor.Red:
        parent_sibling = node.parent_sibling
        parent_sibling_color = RBTreeColor.Black if parent_sibling is None else parent_sibling.color
        # Leaves (None values) are always black, so if there is no parent-sibling then the parent-sibling-color is black
        if parent_sibling_color == RBTreeColor.Red:
            if parent_sibling is not None:
                parent_sibling.color = RBTreeColor.Black
            node.parent.color = RBTreeColor.Black
            node.grandparent.color = RBTreeColor.Red
            reconcile(node.grandparent)
            return
        else:
            grandparent = node.grandparent
            parent = node.parent
            left_of_parent_code = 1 if parent.left == node else 0
            parent_left_of_grandparent_code = 1 if grandparent.left == parent else 0
            strategy_code = left_of_parent_code & parent_left_of_grandparent_code
            try:
                redBlackTreeReconcilliationStrategy[strategy_code](node)
            except KeyError:
                print(f'Strategy Code {strategy_code} could not be resolved')