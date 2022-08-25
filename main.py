

def main():
  tree = Tree(make_bbst(sorted_nodes,0,len(sorted_nodes)-1))
  walk_tree(tree)

class Node:
  def __init__(self, key: int, value: str):
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

def make_bbst(nodes:[], lo:int, hi:int, parent:Node = None):
  mid:int = (hi + lo) // 2
  base_node:Node = nodes[mid]
  base_node.parent = parent
  l_lo = lo
  l_hi= mid-1
  r_lo = mid+1
  r_hi = hi
  if l_lo <= l_hi:
    base_node.left = make_bbst(nodes,l_lo, l_hi, base_node)
  else:
    base_node.left = None

  if r_lo <= r_hi:
    base_node.right = make_bbst(nodes,r_lo, r_hi, base_node)
  else:
    base_node.right = None

  return base_node

def walk_tree(tree:Tree):
  current_node = tree.root
  print(current_node.key)
  while current_node.left or current_node.right:
    parent = current_node.parent
    dir = input("go l or r: ")
    if dir == "l":
      current_node = current_node.left
    elif dir == "r":
      current_node = current_node.right
    print(current_node.key if current_node else "End of the line")
    if dir == "b" or not current_node:
      current_node = parent

if __name__ == "__main__":
  main()