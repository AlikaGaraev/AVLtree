import networkx as nx
import matplotlib.pyplot as plt
from AVLTree import AVLTree, AVLNode

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


def add_edges(G, node, pos=None, x=0, y=0, layer=1):
    if pos is None:
        pos = {node.key: (x, y)}
    else:
        pos[node.key] = (x, y)

    if node.left.is_real_node():
        G.add_edge(node.key, node.left.key)
        l_x, l_y = x - 1 / 2**layer, y - 1
        add_edges(G, node.left, pos, l_x, l_y, layer + 1)

    if node.right.is_real_node():
        G.add_edge(node.key, node.right.key)
        r_x, r_y = x + 1 / 2**layer, y - 1
        add_edges(G, node.right, pos, r_x, r_y, layer + 1)

    return G, pos


def draw_binary_tree(root):
    G = nx.Graph()
    G, pos = add_edges(G, root)
    nx.draw(
        G,
        pos=pos,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_size=12,
    )
    plt.show()


# Example usage:
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(key=1, val="I")
    tree.insert(key=12, val="E")
    tree.insert(key=2, val="K")
    tree.insert(key=11, val="I")
    tree.insert(key=3, val="E")
    tree.insert(key=10, val="K")
    tree.insert(key=4, val="I")
    tree.insert(key=9, val="E")
    tree.insert(key=5, val="K")
    tree.insert(key=8, val="I")
    tree.insert(key=6, val="E")
    tree.insert(key=7, val="K")

    # Draw the binary tree
    draw_binary_tree(tree.root)
