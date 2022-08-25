

class Node:
  def __init__(self, key: int, value, str):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

class Tree:
  def __init__(self, root:Node):
    self.root = root

n1 = Node(1,"1")
n2 = Node(2,"2")
n3 = Node(3,"3")
n4 = Node(4,"4")
n5 = Node(5,"5")
n6 = Node(6,"6")
n7 = Node(7,"7")
n8 = Node(8,"8")
n9 = Node(9,"9")
sorted_nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9] 

def make_bbst(nodes:[], lo:int=None, hi:int=None, parent:Node = None):
  pass


def walk_tree(tree:Tree):
  current_node = tree.root
  print(current_node.key)
  while current_node.left or current_node.right:
    parent = current_node.parent
    dir = input("go l or r")
    if dir == "l":
      current_node = current_node.left
    elif dir == "r":
      current_node = current_node.right
    print(current_node.key)
    if dir == "b" or not current_node:
      current_node = parent