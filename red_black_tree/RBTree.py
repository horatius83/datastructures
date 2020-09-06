from enum import Enum
from typing import Type

class RBTreeColor:
    Red = 1
    Black = 2

class RBTreeNode:
    """Node inside a Red-Black Tree"""
    __slots__ = ['parent', 'left', 'right', 'value', 'color']

    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        self.color = RBTreeColor.Black

    @property
    def grandparent(self):
        if self.parent != None:
            return self.parent.parent

    @property
    def greatgrandparent(self):
        if self.grandparent != None:
            return self.grandparent.parent

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

    @property
    def sibling(self):
        parent = self.parent
        if parent is not None:
            if parent.left == self:
                return parent.right
            else:
                return parent.left

    def insert(self, value):
        if value is None:
            print('Cannot insert nothing')

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                node = RBTreeNode(value)
                node.color = RBTreeColor.Red
                node.parent = self
                self.left = node
                reconcile_insert(node)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                node = RBTreeNode(value)
                node.color = RBTreeColor.Red
                node.parent = self
                self.right = node
                reconcile_insert(node)

    # If you're the root, you cannot delete yourself so what should this do?
    def delete(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.delete(value)
            return None
        if value > self.value:
            if self.right is not None:
                self.right.delete(value)
            return None

        if self.left is not None:
            if self.right is not None:
                pass
            else:
                pass
        elif self.right is not None: 
            parent = self.parent
            if parent is not None:
                if parent.left == self:
                    parent.left = self.right
                    self.right.parent = parent
                else:
                    parent.right = self.right
                    self.right.parent = parent
        else: # This is a leaf   
            parent = self.parent
            if parent is not None:
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None
        self.parent = None
        self.value = None

def left_left_rotation(node: Type[RBTreeNode]):
    greatgrandparent = node.greatgrandparent
    grandparent = node.grandparent
    parent = node.parent
    if greatgrandparent != None:
        if greatgrandparent.left == grandparent:
            greatgrandparent.left = parent
        else:
            greatgrandparent.right = parent
        parent.parent = greatgrandparent
    else:
        parent.parent = None
    grandparent.left = parent.right
    if grandparent.left != None:
        grandparent.left.parent = grandparent
    grandparent.parent = parent
    parent.right = grandparent
    grandparent.color, parent.color = parent.color, grandparent.color

def left_right_rotation(node: Type[RBTreeNode]):
    grandparent = node.grandparent    
    parent = node.parent
    grandparent.left = node
    node.parent = grandparent
    parent.right = node.left
    if parent.right != None:
        parent.right.parent = parent
    node.left = parent
    parent.parent = node
    left_left_rotation(parent)

def right_left_rotation(node: Type[RBTreeNode]):
    grandparent = node.grandparent    
    parent = node.parent
    grandparent.left = node
    node.parent = grandparent
    parent.left = node.right
    if parent.left != None:
        parent.left.parent = parent
    node.right = parent
    parent.parent = node
    right_right_rotation(parent)

def right_right_rotation(node: Type[RBTreeNode]):
    greatgrandparent = node.greatgrandparent
    grandparent = node.grandparent
    parent = node.parent
    if greatgrandparent != None:
        if greatgrandparent.left == grandparent:
            greatgrandparent.left = parent
        else:
            greatgrandparent.right = parent
        parent.parent = greatgrandparent
    else:
        parent.parent = None
    grandparent.right = parent.left
    if grandparent.right != None:
        grandparent.right.parent = grandparent
    grandparent.parent = parent
    parent.left = grandparent
    grandparent.color, parent.color = parent.color, grandparent.color

redBlackTreeReconciliationStrategy  = {
    3: left_left_rotation,
    2: left_right_rotation,
    1: right_left_rotation,
    0: right_right_rotation
}

def reconcile_insert(node: Type[RBTreeNode]):
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
            reconcile_insert(node.grandparent)
            return
        else:
            # depending on the relationship between the node, parent, and grandparent apply different strategies
            # to balance the tree
            grandparent = node.grandparent
            parent = node.parent
            left_of_parent_code = 1 if parent.left == node else 0
            parent_left_of_grandparent_code = 2 if grandparent.left == parent else 0
            strategy_code = left_of_parent_code | parent_left_of_grandparent_code
            try:
                redBlackTreeReconciliationStrategy[strategy_code](node)
            except KeyError:
                print(f'Strategy Code {strategy_code} could not be resolved')