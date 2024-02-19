# username - complete info
# id1      - 323222141
# name1    - Alika Garaev
# id2      - 322868852
# name2    - Ishay Yemini


class AVLNode(object):
    """A class representing a node in an AVL tree"""

    def __init__(self, key, value):
        """
        O(1) - Constructor, you are allowed to add more fields.

        :type key: int | None
        :param key: key of your node
        :type value: any
        :param value: data of your node
        """
        self.key = key
        self.value = value
        if key is not None:
            self.left = AVLNode(None, None)
            self.left.set_parent(self)
            self.right = AVLNode(None, None)
            self.right.set_parent(self)
            self.height = 0
        else:
            self.left = None
            self.right = None
            self.height = -1
        self.parent = None

    def get_left(self):
        """
        O(1) - Returns the left child

        :rtype: AVLNode
        :returns: the left child of self, None if there is no left child (if self is virtual)
        """
        return self.left

    def get_right(self):
        """
        O(1) - Returns the right child

        :rtype: AVLNode
        :returns: the right child of self, None if there is no right child (if self is virtual)
        """
        return self.right

    def get_parent(self):
        """
        O(1) - Returns the parent

        :rtype: AVLNode
        :returns: the parent of self, None if there is no parent
        """
        return self.parent

    def get_key(self):
        """
        O(1) - Returns the key

        :rtype: int | None
        :returns: the key of self, None if the node is virtual
        """
        return self.key

    def get_value(self):
        """
        O(1) - Returns the value

        :rtype: any
        :returns: the value of self, None if the node is virtual
        """
        return self.value

    def get_height(self):
        """
        O(1) - Returns the height

        :rtype: int
        :returns: the height of self, -1 if the node is virtual
        """
        return self.height

    def get_bf(self):
        """
        O(1) - Returns the balance factor

        :rtype: int
        :returns: the balance factor of self, 0 if the node is virtual
        """
        if not self.is_real_node():
            return 0
        return self.get_left().get_height() - self.get_right().get_height()

    def set_left(self, node):
        """
        O(1) - Sets left child, while updating self's height and the child's parent to self

        :type node: AVLNode
        :param node: a node
        """
        if self.is_real_node():
            self.left = node
            self.left.set_parent(self)
            self.set_height(1 + max(self.left.get_height(), self.right.get_height()))

    def set_right(self, node):
        """
        O(1) - Sets right child, while updating self's height and the child's parent to self

        :type node: AVLNode
        :param node: a node
        """
        if self.is_real_node():
            self.right = node
            self.right.set_parent(self)
            self.set_height(1 + max(self.left.get_height(), self.right.get_height()))

    def set_parent(self, node):
        """
        O(1) - Sets parent

        :type node: AVLNode | None
        :param node: a node
        """
        self.parent = node

    def set_value(self, value):
        """
        O(1) - Sets value

        :type value: any
        :param value: data
        """
        self.value = value

    def set_height(self, h):
        """
        O(1) - Sets the height of the node

        :type h: int
        :param h: the height
        """
        self.height = h

    def is_real_node(self):
        """
        O(1) - Checks if self is not a virtual node

        :rtype: bool
        :returns: False if self is a virtual node, True otherwise.
        """
        return self.key is not None


class AVLTree(object):
    """
    A class implementing the ADT Dictionary, using an AVL tree.
    """

    def __init__(self):
        """
        O(1) - Constructor, you are allowed to add more fields.
        """
        self.root = None
        self.tree_size = 0

    def search(self, key):
        """
        O(logn) - Searches for a value in the dictionary corresponding to the key

        :type key: int
        :param key: a key to be searched
        :rtype: AVLNode | None
        :returns: the node if found, otherwise None
        """
        if self.root is None:
            return None
        result = self.tree_position(key)
        if result.get_key() != key:
            return None
        return result

    def insert(self, key, val):
        """
        O(logn) - Inserts val at position i in the dictionary

        :type key: int
        :pre: key currently does not appear in the dictionary
        :param key: key of item that is to be inserted to self
        :type val: any
        :param val: the value of the item
        :rtype: int
        :returns: the number of rebalancing operation due to AVL rebalancing
        """
        new_node = AVLNode(key, val)
        self.tree_size += 1

        if self.root is None or not self.root.is_real_node():
            self.root = new_node
            return 0

        else:
            y = self.tree_position(key)
            old_height = y.get_height()
            if new_node.get_key() < y.get_key():
                y.set_left(new_node)
            else:
                y.set_right(new_node)
            return self.fix_tree(y, old_height)

    def tree_position(self, key):
        """
        O(logn) - Looks for key in the tree and returns the last node encountered

        :type key: int
        :param key: the key of the node searched for
        :rtype: AVLNode | None
        :returns: the node matching the key, or a virtual node
        """
        if self.root is None:
            return None

        node = self.root
        next_node = self.root
        while next_node.is_real_node():
            node = next_node
            if node.get_key() == key:
                return node
            elif node.get_key() > key:
                next_node = node.get_left()
            else:
                next_node = node.get_right()

        return node

    def delete(self, node):
        """
        O(logn) - Deletes node from the dictionary

        :type node: AVLNode
        :pre: node is a real pointer to a node in self
        :rtype: int
        :returns: the number of rebalancing operation due to AVL rebalancing
        """
        if not node.is_real_node():
            return 0

        rotation_count = 0

        if (
            not node.get_left().is_real_node() and not node.get_right().is_real_node()
        ):  # leaf
            new_node = AVLNode(None, None)

        elif (
            not node.get_left().is_real_node() or not node.get_right().is_real_node()
        ):  # has just one child
            new_node = node.get_left()
            if not new_node.is_real_node():
                new_node = node.get_right()

        else:  # has two children
            new_node = node.get_right()
            while new_node.get_left().is_real_node():
                new_node = new_node.get_left()
            rotation_count += self.delete(new_node)
            self.tree_size += 1
            new_node.set_left(node.get_left())
            new_node.set_right(node.get_right())

        self.tree_size -= 1

        if self.root.get_key() == node.get_key():
            self.root = new_node
            self.root.parent = None
            return rotation_count

        parent = node.get_parent()
        old_height = parent.get_height()

        is_left_child = parent.get_left().get_key() == node.get_key()
        if is_left_child:
            parent.set_left(new_node)
        else:
            parent.set_right(new_node)

        return rotation_count + self.fix_tree(parent, old_height)

    def fix_tree(self, node, init_height):
        """
        O(logn) - Fixes the balance of the tree, from provided node and upwards

        :type node: AVLNode
        :param node: the node to balance the tree up from
        :type init_height: int
        :param init_height: the height of the node before changes
        :rtype: int
        :returns: the amount of operations required to rebalance the tree
        """
        parent = node
        old_height = init_height
        rotation_count = 0

        while parent is not None:  # we go up here, so we can't use is_real_node()
            if abs(parent.get_bf()) < 2 and old_height == parent.get_height():
                return rotation_count

            elif abs(parent.get_bf()) == 2:
                if parent.get_bf() == -2:
                    if parent.get_right().get_bf() == 1:  # right rotation before
                        self.right_rotate(parent.get_right())
                        rotation_count += 1
                    self.left_rotate(parent)
                else:
                    if parent.get_left().get_bf() == -1:  # left rotation before
                        self.left_rotate(parent.get_left())
                        rotation_count += 1
                    self.right_rotate(parent)

            rotation_count += 1
            parent = parent.get_parent()
            if parent is not None:
                old_height = parent.get_height()
                parent.set_height(
                    1
                    + max(
                        parent.get_left().get_height(), parent.get_right().get_height()
                    )
                )

        return rotation_count

    def avl_to_array(self):
        """
        O(n) - Returns an array representing dictionary

        :rtype: list
        :returns: a sorted list according to key of tuples (key, value) representing the data structure
        """
        if self.root is None:
            return []
        return self.in_order_scan(self.root)

    def in_order_scan(self, node):
        """
        O(n) - Scans the tree in order

        :type node: AVLNode
        :param node: root of tree to scan
        :rtype: list
        :returns: in order scanned list with tuples (key, value) representing the data structure
        """
        if not node.is_real_node():
            return []
        node_rep = (node.get_key(), node.get_value())
        return (
            self.in_order_scan(node.get_left())
            + [node_rep]
            + self.in_order_scan(node.get_right())
        )

    def size(self):
        """
        O(1) - Returns the number of items in dictionary

        :rtype: int
        :returns: the number of items in dictionary
        """
        return self.tree_size

    def split(self, node):
        """
        O(logn) - Splits the dictionary at the i'th index

        :type node: AVLNode
        :pre: node is in self
        :param node: The intended node in the dictionary according to whom we split
        :rtype: list
        :returns: a list [left, right], where left is an AVLTree representing the keys in the
            dictionary smaller than node.key, right is an AVLTree representing the keys in the
            dictionary larger than node.key
        """
        left_subtree = self.get_sub_tree(node.get_left())
        right_subtree = self.get_sub_tree(node.get_right())

        parent = node.get_parent()
        while parent is not None:
            if parent.get_key() < node.get_key():
                old_left_subtree = left_subtree
                left_subtree = self.get_sub_tree(parent.get_left())
                left_subtree.join(
                    old_left_subtree, parent.get_key(), parent.get_value()
                )
            else:
                right_subtree.join(
                    self.get_sub_tree(parent.get_right()),
                    parent.get_key(),
                    parent.get_value(),
                )
            parent = parent.get_parent()

        return [left_subtree, right_subtree]

    @staticmethod
    def get_sub_tree(node):
        """
        O(1) - Returns the subtree where node is the root

        :param node: Node
        :return: AVLTree
        """
        tree = AVLTree()
        if node.is_real_node():
            tree.root = node
            tree.root.parent = None
        return tree

    def join(self, tree2, key, val):
        """
        O(logn) - Joins self with key and another AVLTree

        :type tree2: AVLTree
        :param tree2: a dictionary to be joined with self
        :type key: int
        :param key: The key separating self with tree2
        :type val: any
        :param val: The value attached to key
        :pre: all keys in self are smaller than key and all keys in tree2 are larger than key
        :rtype: int
        :returns: the absolute value of the difference between the height of the AVL trees joined
        """
        new_node = AVLNode(key, val)
        a = self.root
        b = tree2.get_root()
        self.tree_size = self.tree_size + 1 + tree2.size()

        if a is None or b is None:
            if a is None:
                self.root = b
            diff = self.root.get_height() if self.root is not None else 0
            self.insert(key, val)
            return diff

        diff = abs(a.get_height() - b.get_height())
        old_height = 0

        if a.get_height() == b.get_height():
            self.root = new_node

        elif a.get_height() > b.get_height():
            self.root = a
            while a.get_height() > b.get_height():
                a = a.get_right()
            old_height = a.get_parent().get_height()
            a.get_parent().set_right(new_node)

        else:
            self.root = b
            while a.get_height() < b.get_height():
                b = b.get_left()
            old_height = b.get_parent().get_height()
            b.get_parent().set_left(new_node)

        new_node.set_left(a)
        new_node.set_right(b)

        if diff == 0:
            return diff

        parent = new_node.get_parent()
        self.fix_tree(parent, old_height)

        return diff

    def get_root(self):
        """
        O(1) - Returns the root of the tree representing the dictionary


        :rtype: AVLNode
        :returns: the root, None if the dictionary is empty
        """
        return self.root

    def rotate(self, x, right=False):
        """
        O(1) - Performs a rotation, by default to the left, but if "right" is true then to the right

        :type x: AVLNode
        :param x: the old root of the sub-tree to be rotated
        :type right: bool
        :param right: whether to perform a right rotation
        :rtype: AVLNode
        :returns: the new root of the sub-tree
        """
        if not x.is_real_node():
            return x

        old_parent = x.get_parent()

        if right:
            y = x.get_left()
            z = y.get_right()
            x.set_left(z)
            y.set_right(x)
        else:
            y = x.get_right()
            z = y.get_left()
            x.set_right(z)
            y.set_left(x)

        if x.get_key() == self.root.get_key():
            self.root = y
            self.root.set_parent(None)
        elif x.get_key() == old_parent.get_left().get_key():
            old_parent.set_left(y)
        else:
            old_parent.set_right(y)

        return y

    def left_rotate(self, x):
        """
        O(1) - Performs a left rotation

        :type x: AVLNode
        :param x: the old root of the sub-tree to be rotated
        :rtype: AVLNode
        :returns: the new root of the tree
        """
        return self.rotate(x)

    def right_rotate(self, x):
        """
        O(1) - Performs a right rotation

        :type x: AVLNode
        :param x: the old root of the sub-tree to be rotated
        :rtype: AVLNode
        :returns: the new root of the tree
        """
        return self.rotate(x, True)
