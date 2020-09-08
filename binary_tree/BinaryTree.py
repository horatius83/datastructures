from typing import Type, Any, Optional

class BinaryTreeNode:
    __slots__ = ['parent', 'left', 'right', 'value', 'color']

    parent: Optional[BinaryTreeNode] = None
    left: Optional[BinaryTreeNode] = None
    right: Optional[BinaryTreeNode] = None
    value: Any = None

    def __init__(self, value):
        self.value = value

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

    def insert(self, value: Any) -> BinaryTreeNode:
        insert(self, value)

def insert(node: Type[BinaryTreeNode], value: Any):
    if value < node.value:
        if value.left:
            insert(value.left, value)
        else:
            pass