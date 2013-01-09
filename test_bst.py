import unittest
from bst import *


class EmptyTreeTestCase(unittest.TestCase):
    '''Test for an empty tree'''

    def setUp(self):
        '''Generate an empty tree to test.'''
        self.tree = BSTree()

    def tearDown(self):
        '''Perform cleanup operations.'''
        pass

    def testTreeRoot(self):
        '''Verify that the root of the tree is null.'''
        self.assertEqual(self.tree.root, None)

    def testHeight(self):
        '''Verify that the tree has height of 0.'''
        self.assertEqual(self.tree.height(), 0)

    def testRange(self):
        '''Verify that the any range of nodes results in an empty list.'''
        result = self.tree.range(0, 10)
        self.assertEqual(len(result), 0)

    def testSearch(self):
        '''Verify that searching for any value of node will return None.'''
        self.assertEqual(self.tree.search(1), None)

    def testIOP(self):
        '''Verify that there is no IOP for any node in the tree.'''
        self.assertEqual(in_order_predecessor(self.tree.root), None)

    def testIOS(self):
        '''Verify that there is no IOS for any node in the tree.'''
        self.assertEqual(in_order_successor(self.tree.root), None)

    def testDelete(self):
        '''Verify that deletion always returns None.'''
        self.assertEqual(self.tree.delete(2), None)


class OneNodeTestCase(unittest.TestCase):
    '''Test for a tree containing one node.'''

    def setUp(self):
        '''Generate a tree containing one node to test.'''
        self.tree = BSTree(BTNode(5))

    def tearDown(self):
        '''Perform cleanup operations.'''
        pass

    def testTreeRoot(self):
        '''Verify that the root has a value of 5.'''
        self.assertEqual(self.tree.root.value, 5)

    def testHeight(self):
        '''Verify that the height of the tree is 1.'''
        self.assertEqual(self.tree.height(), 1)

    def testRange(self):
        '''Verify that the only node found by range() is the root.'''
        # Try looking for values that exist.
        result = self.tree.range(4, 6)
        self.assertEqual(result[0].value, 5)
        self.assertEqual(len(result), 1)
        # Try looking for values that do not exist.
        result = self.tree.range(10, 10)
        self.assertEqual(len(result), 0)

    def testSearch(self):
        '''Verify that only a search for a node with value 5 will work.'''
        self.assertEqual(self.tree.search(1), None)
        self.assertEqual(self.tree.search(5).value, 5)

    def testIOP(self):
        '''Verify that there is no IOP for the root.'''
        self.assertEqual(in_order_predecessor(self.tree.root), None)

    def testIOS(self):
        '''Verify that there is no IOS for the root.'''
        self.assertEqual(in_order_successor(self.tree.root), None)

    def testDelete(self):
        '''Verify that only deletion of a node with a value of 5 works.'''
        self.tree.delete(2)
        self.assertEqual(self.tree.root.value, 5)
        self.assertEqual(self.tree.root.left, None)
        self.assertEqual(self.tree.root.right, None)
        self.tree.delete(5)
        self.assertEqual(self.tree.root, None)


class ComplexTreeTestCase(unittest.TestCase):
    '''Test for a tree with both left and right children.'''

    def setUp(self):
        '''Generate a tree to test.
                8
            6       7
        5
                    4
                3
            2
                1
        '''
        self.tree = BSTree()
        for val in [5, 2, 6, 1, 3, 8, 4, 7]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''
        pass

    def testTreeRoot(self):
        '''Verify that the root has a value of 5.'''
        self.assertEqual(self.tree.root.value, 5)

    def testHeight(self):
        '''Verify that the height of the tree is correct.'''
        self.assertEqual(self.tree.height(), 4)

    def testRange(self):
        '''Verify that ranges existing in the tree return a correct list.'''
        # Try looking for values that exist.
        result = self.tree.range(4, 6)
        self.assertEqual(result[0].value, 4)
        self.assertEqual(result[1].value, 5)
        self.assertEqual(result[2].value, 6)
        self.assertEqual(len(result), 3)
        # Try looking for values that do not exist.
        result = self.tree.range(10, 10)
        self.assertEqual(len(result), 0)

    def testSearch(self):
        '''Verify that values in the tree can be found.'''
        self.assertEqual(self.tree.search(20), None)
        self.assertEqual(self.tree.search(5).value, 5)
        self.assertEqual(self.tree.search(4).value, 4)
        self.assertEqual(self.tree.search(7).value, 7)

    def testIOP(self):
        '''Verify that the left-most node in the tree does not have an IOP
        and that the IOP of 7 is 6.'''
        self.assertEqual(in_order_predecessor(self.tree.root.left.left), None)
        self.assertEqual(in_order_predecessor( \
            self.tree.root.right.right.left), \
                         self.tree.root.right)

    def testIOS(self):
        '''Verify that the right-most node in the tree does not have an IOS
        and that the IOS of 2 is 3.'''
        self.assertEqual(in_order_successor(self.tree.root.right.right), None)
        self.assertEqual(in_order_successor(self.tree.root.left), \
                         self.tree.root.left.right)

    def testDelete(self):
        '''Verify that deletion works in the case of a leaf, a node with
        one subtree, and a node with two subtrees.'''
        self.tree.delete(1)
        self.assertEqual(self.tree.root.left.value, 2)
        self.assertEqual(self.tree.root.left.left, None)
        self.tree.delete(8)
        self.assertEqual(self.tree.root.right.right.value, 7)
        self.assertEqual(self.tree.root.right.right.left, None)
        self.tree.delete(5)
        self.assertEqual(self.tree.root.value, 4)
        self.assertEqual(self.tree.root.left.value, 2)


class BTNodeTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''Generate a tree to test.
                9
            7
        5
            3
                2
        '''
        self.tree = BSTree()
        for val in [5, 7, 3, 2, 9]:
            self.tree.insert(val)
        self.five = self.tree.root
        self.three = self.tree.root.left
        self.two = self.tree.root.left.left
        self.seven = self.tree.root.right
        self.nine = self.tree.root.right.right

    def tearDown(self):
        '''Perform cleanup actions.'''
        pass

    def testSetLeft(self):
        '''Verify that the correct nodes are left children.'''
        self.assertEqual(self.five.left, self.three)
        self.assertEqual(self.three.left, self.two)

    def testSetRight(self):
        '''Verify that the correct nodes are right children.'''
        self.assertEqual(self.five.right, self.seven)
        self.assertEqual(self.seven.right, self.nine)

    def testTreeRoot(self):
        '''Verify that 5 is the root of the tree.'''
        self.assertEqual(self.tree.root.value, 5)

    def testLeftChild(self):
        '''Verify that only 3 and 2 are left children.'''
        self.assertFalse(self.five.is_left_child())
        self.assertTrue(self.two.is_left_child())
        self.assertTrue(self.three.is_left_child())
        self.assertFalse(self.seven.is_left_child())
        self.assertFalse(self.nine.is_left_child())

    def testRightChild(self):
        '''Verify that only 7 and 9 are right children.'''
        self.assertTrue(self.seven.is_right_child())
        self.assertTrue(self.nine.is_right_child())
        self.assertFalse(self.three.is_right_child())
        self.assertFalse(self.five.is_right_child())
        self.assertFalse(self.two.is_right_child())

    def testLeafChild(self):
        '''Verify that only 2 and 9 are leaf nodes.'''
        self.assertFalse(self.five.is_leaf())
        self.assertFalse(self.three.is_leaf())
        self.assertFalse(self.seven.is_leaf())
        self.assertTrue(self.two.is_leaf())
        self.assertTrue(self.nine.is_leaf())

    def testNodeHeight(self):
        '''Verify the that all nodes have the correct height.'''
        self.assertEqual(self.five.height(), 3)
        self.assertEqual(self.seven.height(), 2)
        self.assertEqual(self.three.height(), 2)
        self.assertEqual(self.two.height(), 1)
        self.assertEqual(self.nine.height(), 1)

    def testNodeDepth(self):
        '''Verify that all nodes have the correct depth.'''
        self.assertEqual(self.five.depth(), 1)
        self.assertEqual(self.seven.depth(), 2)
        self.assertEqual(self.three.depth(), 2)
        self.assertEqual(self.two.depth(), 3)
        self.assertEqual(self.nine.depth(), 3)


def BTNode_suite():
    """Return a test suite for bst."""

    return unittest.TestLoader().loadTestsFromTestCase(BTNodeTestCase)


def EmptyTree_suite():
    '''Return a test suite for bst.'''

    return unittest.TestLoader().loadTestsFromTestCase(EmptyTreeTestCase)


def OneNodeTree_suite():
    '''Return a test suite for bst.'''

    return unittest.TestLoader().loadTestsFromTestCase(OneNodeTestCase)


def ComplexTree_suite():
    '''Return a test suite for bst.'''

    return unittest.TestLoader().loadTestsFromTestCase(ComplexTreeTestCase)


if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(BTNode_suite())
    runner.run(EmptyTree_suite())
    runner.run(OneNodeTree_suite())
    runner.run(ComplexTree_suite())
