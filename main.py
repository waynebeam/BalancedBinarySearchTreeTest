import time

def main():
  sorted_nodes = []
  tree_size = int(input("What size integer tree? \n"))
  start_time = time.time()
  for i in range(tree_size):
    node = Node(i, f"{i}")
    sorted_nodes.append(node)  
  tree = Tree(make_bbst(sorted_nodes,0,len(sorted_nodes)-1))
  end_time = time.time()
  print(f"{(end_time-start_time)*1000} milisecond setup time")
  
  while(choice := input("Walk, update, count, height,look up, print all, or draw?: ")) != "q":
    if choice == "h":
      print(f"tree is {tree.find_height(tree.root)} levels tall")
    if choice == "w":
      walk_tree(tree)
      
    if choice == "c":
      print(f'{tree.count_nodes(tree.root)} nodes')
      
    if choice == "u":
      key = int(input("Which key?: "))
      value = input("What's the new value?: ")
      tree[key] = value
      
    if choice == "d":
      tree.draw_tree(tree.root)
    if choice == "p":
      print(tree.list_all(tree.root))
      
    if choice == "l":
      key = int(input("Which key?: "))
      result = tree.search(tree.root,key)
      print(result.value + str(result.key) if result is not None else "No such thing")
   
    # if choice == "s":
    #   target_key = int(input("Which key?: "))
    #   brute_search_tree(target_key,sorted_nodes)
    #   tree.search(target_key)

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
    self.all_nodes = []

  def find_height(self, node: Node):
    if node is None:
      return 0
    return 1 + max(self.find_height(node.left), self.find_height(node.right))

  def count_nodes(self, node:Node):
    if node is None:
      return 0
    return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

  def __setitem__(self, key, value):
    result = self.search(self.root, key)
    if result is not None:
      self.update(result,value)
    else:
      print("insert")
      self.insert(self.root,key,value)
      
  def insert(self,node,key, value):
    if node is None:
      node = Node(key,value)
      return node

    if key < node.key:
      node.left = self.insert(node.left,key,value)    
      return node
    if key > node.key:
      node.right = self.insert(node.right, key, value)
      return node
  
  def search(self, node:Node, target_key:int):
    if node is None:
      return None
    if node.key == target_key:
      return node
    if target_key < node.key:
      return self.search(node.left, target_key)
    if target_key > node.key:
      return self.search(node.right, target_key)
    

  def update(self,node, value):
    
      node.value = value
    

  def list_all(self, node:Node = None):
    if not node:
      return []  
    return (self.list_all(node.left)
           + [(node.key, node.value)]
           + self.list_all(node.right))

  def draw_tree(self, node, level=0, space='\t'):
    if node is None:
      print(space*level + 'x')
      return

    if node.left is None and node.right is None:
      print(space*level + str(node.key))
      return

    self.draw_tree(node.right,level+1)
    print(space*level + str(node.key))
    self.draw_tree(node.left, level+1)


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


def brute_search_tree(target_key, nodes:[]):
  count = 0
  start_time= time.time()
  for node in nodes:
    count += 1
    if node.key == target_key:
      end_time= time.time()
      print(f"\nfound {target_key} \nin {count} steps by brute force \nin {(end_time-start_time)*1000} miliseconds")
    

def walk_tree(tree:Tree):
  current_node = tree.root
  print(current_node.key)
  while current_node.left or current_node.right:
    parent = current_node.parent
    dir = input("go l or r: ")
    if dir == "l" and current_node.left:
      current_node = current_node.left
      print('move to ', current_node.key)
    elif dir == "r" and current_node.right:
      current_node = current_node.right
      print('move to ', current_node.key)

    else: 
      print('End of branch. Staying on ',current_node.key )
      if dir == "b":
        current_node = parent

  print(f"Arrived at {current_node.key}. End of the tree")
if __name__ == "__main__":
  main()