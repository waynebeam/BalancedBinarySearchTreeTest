import time

def main():
  sorted_nodes = []
  for i in range(1000000):
    node = Node(i, f"{i}")
    sorted_nodes.append(node)  
  tree = Tree(make_bbst(sorted_nodes,0,len(sorted_nodes)-1))
  
  while(choice := input("Walk, search, or brute search?: ")) != "q":
    if choice == "w":
      walk_tree(tree)
    if choice == "b":
      target_key = int(input("Which key?: "))
      brute_search_tree(target_key, sorted_nodes)
    if choice == "s":
      target_key = int(input("Which key?: "))
      tree.search(target_key)

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

  def search(self, target_key:int):
    count = 0
    start_time= time.time()
    current_node = self.root
    while current_node.key != target_key:
      count += 1
      if target_key < current_node.key:
        current_node = current_node.left
      if target_key > current_node.key:
        current_node = current_node.right
    end_time= time.time()
    print(f"found {target_key} in {count} steps using the tree in {(end_time-start_time)*1000} seconds")



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
      print(f"found {target_key} in {count} steps by brute force in {(end_time-start_time)*1000} seconds")
    

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