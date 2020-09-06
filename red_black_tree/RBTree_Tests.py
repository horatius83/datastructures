import unittest
from RBTree import RBTreeNode, RBTreeColor, reconcile

class TestRBTree(unittest.TestCase):
    def test_nodes_default_to_red(self):
        value = 'test'
        n = RBTreeNode(value)
        self.assertEqual(n.color, RBTreeColor.Red)
        self.assertEqual(n.value, value)
        self.assertEqual(n.left, None)
        self.assertEqual(n.right, None)

    def test_root_will_reconcile_to_black(self):
        n = RBTreeNode('test', is_root = True)
        reconcile(n)
        self.assertEqual(n.color, RBTreeColor.Black)

    def test_root_has_no_grandparent_or_parent_sibling(self):
        n = RBTreeNode('test')
        self.assertEqual(n.grandparent, None)
        self.assertEqual(n.parent_sibling, None)

    def test_root_has_grandparent(self):
        n = RBTreeNode(1)
        p = RBTreeNode(2, left=n)
        gp = RBTreeNode(3, right=p, is_root=True)
        self.assertEquals(n.parent, p)
        self.assertEquals(p.left, n)
        self.assertEqual(n.grandparent, gp)
        self.assertEquals(gp.right, p)

    def test_insert_less_than(self):
        n = RBTreeNode(5)
        less_than_node = RBTreeNode(4, is_root=True)
        n.insert(less_than_node)
        self.assertEquals(n.left, less_than_node)
        self.assertEquals(less_than_node.parent, n)

    def test_insert_greater_than(self):
        n = RBTreeNode(5, is_root=True)
        greater_than_node = RBTreeNode(6)
        n.insert(greater_than_node)
        self.assertEquals(n.right, greater_than_node)
        self.assertEquals(greater_than_node.parent, n)

    def test_insert_equal(self):
        n = RBTreeNode(5, is_root=True)
        equal_node = RBTreeNode(5)
        n.insert(equal_node)
        self.assertEquals(n.right, equal_node)
        self.assertEquals(equal_node.parent, n)

if __name__ == '__main__':
    unittest.main()