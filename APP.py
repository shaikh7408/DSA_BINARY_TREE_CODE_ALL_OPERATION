from node import Node
from binary_tree import Binary_Tree
tree=Binary_Tree(Node(5))
nodes=[7,6,8,9,10,22,1]
for n in nodes:
    tree.add(Node(n))

tree.deleting_node()
tree.Inorder()
#tree.preorder()
