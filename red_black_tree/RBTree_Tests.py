import unittest
from RBTree import RBTreeNode, RBTreeColor, reconcile

class TestRBTree(unittest.TestCase):
    def test_root(self):
        value = 'value'

        root = RBTreeNode(value)

        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertEqual(root.parent, None)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)
        self.assertEqual(root.value, value)

    def test_insert_less_than(self):
        root = RBTreeNode(5)
        value = 4

        root.insert(value)

        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertNotEqual(root.left, None)
        self.assertEqual(root.left.parent, root)
        self.assertEqual(root.left.color, RBTreeColor.Red)
        self.assertEqual(root.left.value, value)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)

    def test_insert_greater_than(self):
        root = RBTreeNode(5)
        value = 6

        root.insert(value)

        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertNotEqual(root.right, None)
        self.assertEqual(root.right.parent, root)
        self.assertEqual(root.right.color, RBTreeColor.Red)
        self.assertEqual(root.right.value, value)
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right, None)

    def test_insert_equal(self):
        root = RBTreeNode(5)
        value = 5

        root.insert(value)

        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertNotEqual(root.right, None)
        self.assertEqual(root.right.parent, root)
        self.assertEqual(root.right.color, RBTreeColor.Red)
        self.assertEqual(root.right.value, value)
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right, None)

    def test_recoloring(self):
        root = RBTreeNode(5)
        root.insert(2)
        root.insert(7)
        root.insert(1)

        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertEqual(root.left.color, RBTreeColor.Black)
        self.assertEqual(root.right.color, RBTreeColor.Black)
        self.assertEqual(root.left.left.color, RBTreeColor.Red)

    def test_left_left_reconciliation_strategy_with_no_greatgrandparent(self):
        root = RBTreeNode(5)
        root.insert(4)
        root.insert(3)

        self.assertEqual(root.parent.value, 4)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)
        self.assertEqual(root.parent.right, root)
        self.assertEqual(root.parent.left.value, 3)
        self.assertEqual(root.parent.left.left, None)
        self.assertEqual(root.parent.left.right, None)
        self.assertEqual(root.parent.left.parent, root.parent)

    def test_left_right_reconciliation_strategy_with_no_greatgrandparent(self):
        root = RBTreeNode(5)
        for value in [7, 2, 0, 1]:
            root.insert(value)
        self.assertEqual(root.value, 5)
        self.assertEqual(root.parent, None)
        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertEqual(root.left.value, 1)
        self.assertEqual(root.left.color, RBTreeColor.Black)
        self.assertEqual(root.left.parent, root)
        self.assertEqual(root.right.value, 7)
        self.assertEqual(root.right.color, RBTreeColor.Black)
        self.assertEqual(root.right.parent, root)
        self.assertEqual(root.left.left.value, 0)
        self.assertEqual(root.left.left.color, RBTreeColor.Red)
        self.assertEqual(root.left.left.parent, root.left)
        self.assertEqual(root.left.right.value, 2)
        self.assertEqual(root.left.right.color, RBTreeColor.Red)
        self.assertEqual(root.left.right.parent, root.left)

    def test_right_right_reconciliation_strategy_with_no_greatgrandparent(self):
        root = RBTreeNode(5)
        root.insert(6)
        root.insert(7)
        self.assertEqual(root.value, 5)
        self.assertEqual(root.color, RBTreeColor.Red)
        self.assertEqual(root.parent.left, root)
        self.assertEqual(root.parent.value, 6)
        self.assertEqual(root.parent.color, RBTreeColor.Black)
        self.assertEqual(root.parent.right.value, 7)
        self.assertEqual(root.parent.right.color, RBTreeColor.Red)

    def test_right_left_reconciliation_strategy_with_no_greatgrandparent(self):
        root = RBTreeNode(5)
        for value in [7,2,10,9]:
            root.insert(value)
        self.assertEqual(root.value, 5)
        self.assertEqual(root.color, RBTreeColor.Black)
        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.left.color, RBTreeColor.Black)
        self.assertEqual(root.left.parent, root)
        self.assertEqual(root.right.value, 9)
        self.assertEqual(root.right.color, RBTreeColor.Black)
        self.assertEqual(root.right.parent, root)
        self.assertEqual(root.right.left.value, 7)
        self.assertEqual(root.right.left.color, RBTreeColor.Red)
        self.assertEqual(root.right.left.parent, root.right)
        self.assertEqual(root.right.right.value, 10)
        self.assertEqual(root.right.right.color, RBTreeColor.Red)
        self.assertEqual(root.right.right.parent, root.right)



if __name__ == '__main__':
    unittest.main()