# username - complete info
# id1      - complete info 
# name1    - complete info 
# id2      - 322868852
# name2    - Ishay Yemini


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields. 

    @type key: int | None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1  # Balance factor

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """
    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """
    def get_right(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """
    def get_parent(self):
        return self.parent

    """returns the key

    @rtype: int | None
    @returns: the key of self, None if the node is virtual
    """
    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """
    def get_value(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """
    def get_height(self):
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """
    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """
    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """
    def set_parent(self, node):
        self.parent = node

    """sets value

    @type value: any
    @param value: data
    """
    def set_value(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """
    def set_height(self, h):
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def is_real_node(self):
        return self.key is None


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.  
    """
    def __init__(self):
        self.root = None

    # add your fields here

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """
    def search(self, key):
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def insert(self, key, val):
        return -1

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def delete(self, node):
        return -1

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """
    def avl_to_array(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """
    def size(self):
        return -1

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """
    def split(self, node):
        return None

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def join(self, tree2, key, val):
        return None

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """
    def get_root(self):
        return None

    """performs a rotation, by default to the left, but if "right" is true than to the right

    @type x: AVLNode 
    @param x: the old root of the sub-tree to be rotated
    @type right: bool 
    @param right: whether to perform a right rotation
    @rtype: AVLNode
    @returns: the new root of the sub-tree
    """
    def rotate(self, x, right=False):
        children = ["right", "left"]
        if right:
            children.reverse()

        # Perform rotation
        y = x[children[0]]
        z = y[children[1]]
        x[children[0]] = z
        y[children[1]] = x

        # Update heights
        x.height = 1 + max(x.left.get_height(), x.right.get_height())
        y.height = 1 + max(y.left.get_height(), y.right.get_height())

        # Return the new root
        return y

    """performs a left rotation
    
    @rtype: AVLNode
    @returns: the new root of the tree
    """
    def left_rotate(self, x):
        return self.rotate(x)

    """performs a right rotation

    @type x: AVLNode 
    @param x: the old root of the sub-tree to be rotated
    @rtype: AVLNode
    @returns: the new root of the tree
    """
    def right_rotate(self, x):
        return self.rotate(x, True)
