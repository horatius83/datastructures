import unittest
from RBTree import RBTreeNode, RBTreeColor, reconcile

class TestRBTree(unittest.TestCase):
    def test_nodes_default_to_red(self):
        n = RBTreeNode(None, None, None, 'test')
        self.assertEqual(n.color, RBTreeColor.Red)

    def test_root_will_reconcile_to_black(self):
        n = RBTreeNode(None, None, None, 'test')
        reconcile(n)
        self.assertEqual(n.color, RBTreeColor.Black)

    def test_root_has_no_grandparent(self):
        n = RBTreeNode(None, None, None, 'test')
        self.assertEqual(n.grandparent, None)

    def test_root_has_no_parent_sibling(self):
        n = RBTreeNode(None, None, None, 'test')
        self.assertEqual(n.parent_sibling, None)


if __name__ == '__main__':
    unittest.main()