class BTNode:
    '''A generic binary tree node that keeps a value and pointers to
    a left child, right child and parent.'''

    def __init__(self, v, p=None):
        '''(BTNode, object, BTNode) -> NoneType
        A new BTNode with value v, no left or right
        children and parent p. p is None by default.'''

        self.value = v
        self.left = None
        self.right = None
        self.parent = p

    def __str__(self):
        '''(BTNode) -> str
        Return the string representation of self.
        This method is called by print() and str()
        NOTE: This method is complete.'''

        return str(self.value)

    def __repr__(self):
        '''(BTNode) -> str
        Return the internal string representation of self.
        This method is called when a list of BTNodes is
        printed.
        NOTE: This method is complete.'''

        return "BTNode: {}".format(self.value)

    def set_right(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the right child of self.
        Set bidirectional links correctly.'''

        self.right = n
        if n:
            n.parent = self

    def set_left(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the left child of self.
        Set bidirectional links correctly.'''

        self.left = n
        if n:
            n.parent = self

    def is_left_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self is
        the left child of its parent.'''

        return self.parent and self.parent.left == self

    def is_right_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self is
        the right child of its parent.'''

        return self.parent and self.parent.right == self

    def is_leaf(self):
        '''(BTNode) -> bool
        Return True iff self is a leaf node.'''

        return self.right == None and self.left == None

    def height(self):
        '''(BTNode) -> int
        Return the height of self. Height is defined as the length of the
        longest path by number of nodes from self to a leaf.
        The height of a leaf node is 1.'''

        if self.is_leaf():
            return 1
        #If no left child exists, return the height of the right child.
        elif self.right and not self.left:
            return self.right.height() + 1
        #If no right child exists, return the height of the left child.
        elif self.left and not self.right:
            return self.left.height() + 1
        #Otherwise, return the maximum of the height of the children.
        else:
            return max(self.right.height() + 1, self.left.height() + 1)

    def depth(self):
        '''(BTNode) -> int
        Return the depth of self. Depth is defined as the length of the
        path by number of nodes from the root of the tree to self.
        The depth of a root node is 1.'''

        if self.parent == None:
            return 1
        return self.parent.depth() + 1


class BSTree:
    '''A Binary Search Tree that conforms to the BST property at every step.
    The BST property states that for every node with value k, its left child
    is a (possibly empty) BST with values strictly less than k and its right
    child is a (possibly empty) BST with values strictly greater than k.'''

    def __init__(self, root=None):
        '''(BSTree, BTNode) -> NoneType
        Create a new BST with an optional root.
        NOTE: This method is complete.'''

        self.root = root

    def print_tree(self):
        '''(BSTree) -> NoneType
        Print tree recursively (used for testing purposes)
        NOTE: This method is complete.'''

        _print_tree(self.root, 1)

    def insert(self, v):
        '''(BSTree, object) -> NoneType
        Insert a new node with value v into self. Do not duplicate values.
        NOTE: This method is complete.'''

        if not self.root:
            self.root = BTNode(v)
            return
        _insert(self.root, v)

    def height(self):
        '''(BSTree) -> int
        Return the height of this tree.'''

        if self.root == None:
            return 0
        return self.root.height()

    def search(self, v):
        '''(BSTree, object) -> BTNode
        Return BTNode with value v if it exists in the tree. Return None if no
        such node exists. Assume unique node values.
        NOTE: This method is complete.'''

        return _search(self.root, v)

    def range(self, v_start, v_end):
        '''(BSTree, object, object) -> list
        Return a list of Node objects with values between v_start and
        v_end inclusive. Assume v_start and v_end can be ordered and
        v_start <= v_end. v_start and v_end may not be values that
        exist in the tree.
        NOTE: This method is complete.'''

        return _range(self.root, v_start, v_end)

    def delete(self, v):
        '''(BSTree, object) -> NoneType
        Delete node with value v from self. Change root if required.
        NOTE: This method is complete.'''

        self.root = _delete(self.root, v)


## HELPER RECURSIVE FUNCTIONS

def _print_tree(root, depth):
    '''(BTNode, int) -> NoneType
    Print the left subtree of root, print root preceded by four spaces for
    every unit of depth, then print the right subtree of root.
    depth is the depth of root.
    NOTE: This function is complete.'''

    if root is None:
        return
    _print_tree(root.right, depth + 1)
    print("    " * (depth - 1) + str(root))
    _print_tree(root.left, depth + 1)


def _insert(root, v):
    '''(BTNode, obj) -> NoneType
    Insert a new node with value v into BST rooted at root.
    Do not allow duplicates.
    NOTE: This function is complete.'''

    if root.value == v:
        return
    if v < root.value:
        if root.left:
            _insert(root.left, v)
        else:
            root.set_left(BTNode(v))
    elif v > root.value:
        if root.right:
            _insert(root.right, v)
        else:
            root.set_right(BTNode(v))


def _search(root, v):
    '''(BTNode, object) -> BTNode
    Return BTNode with value v if it exists in subtree rooted at
    root. Return None if no such BTNode exists.'''

    if not root:
        return
    elif root.value == v:
        return root
    # If the current node's value is less than v, look in the right subtree.
    elif root.value < v:
        return _search(root.right, v)
    # If the current node's value is greater than v, look in the left subtree.
    elif root.value > v:
        return _search(root.left, v)


def _range(root, v_start, v_end):
    '''(BTNode, int, int) -> list
    Return an in-order list of BTNodes that have values between
    v_start and v_end, inclusive in subtree rooted at root.'''

    val = []
    if not root:
        return []
    # If the desired values are all greater than root, look in the
    # right subtree.
    if v_start > root.value:
        return _range(root.right, v_start, v_end)
    # If the desired values are all smaller than root, look in the
    # left subtree.
    elif v_end < root.value:
        return _range(root.left, v_start, v_end)
    else:
        # Return a list of the left subtree, the root, and the right subtree.
        left_sub = _range(root.left, v_start, v_end)
        if left_sub:
            val.extend(left_sub)

        val.append(root)

        right_sub = _range(root.right, v_start, v_end)
        if right_sub:
            val.extend(right_sub)

        return val


def _delete(root, v):
    '''(BTNode, object) -> BTNode
    Delete BTNode with value v from subtree rooted at root.
    Return root of subtree. Do nothing if value doesn't exist in subtree.'''

    # Search for node with value v.
    if not root:
        return None
    if root.value > v:
        root.set_left(_delete(root.left, v))
        return root
    elif root.value < v:
        root.set_right(_delete(root.right, v))
        return root
    else:
        # Node has two subtrees.
        if root.right and root.left:
            if root.right.height() <= root.left.height():
                IOP = in_order_predecessor(root)
                root.set_left(_delete(root.left, IOP.value))
                root.value = IOP.value
                return root
            else:
                IOS = in_order_successor(root).value
                root.set_right(_delete(root.right, IOS.value))
                root.value = IOS.value
                return root
        # Node has one subtree.
        elif root.right or root.left:
            if root.right:
                return root.right
            elif root.left:
                return root.left
        # Node is a leaf.
        elif root.is_leaf():
            return None
        else:
            # Node with value v doesn't exist in subtree rooted at root.
            return


## NEIGHBOURS FUNCTIONS


def in_order_predecessor(node):
    '''(BTNode) -> BTNode
    Return the in-order predecessor of node.
    Return None if node is leftmost.'''

    if node == None:
        return
    # If a left subtree exists, follow every right pointer until there are no
    # more, and return the node.
    if node.left:
        node = node.left
        while node:
            if node.right == None:
                return node
            node = node.right
    # Otherwise, return the parent of the first right child
    # that is an ancestor.
    else:
        while node:
            if node.is_right_child():
                return node.parent
            node = node.parent
        # If at root, return None.
        return


def in_order_successor(node):
    '''(BTNode) -> BTNode
    Return the in-order successor of node.
    Return None if node is rightmost.'''

    if node == None:
        return
    # If a right subtree exists, follow every left pointer until there are no
    # more, and return the node.
    if node.right:
        node = node.right
        while node:
            if node.left == None:
                return node
            node = node.left
    # Otherwise, return the parent of the first right child
    # that is an ancestor.
    else:
        while node:
            if node.is_left_child():
                return node.parent
            node = node.parent
        # If at root, return None.
        return


if __name__ == '__main__':
    pass
