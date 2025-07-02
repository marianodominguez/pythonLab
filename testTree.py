from algorithms.BinaryTree import Tree
import random
from functools import reduce

mytree = Tree()
list = list(range(50))
random.shuffle(list)
#print(list)

for i in list:
    mytree.put(i)

print("inorder: ", mytree.inorder(mytree.root))
print("preorder: ", mytree.preorder(mytree.root))
print("postorder: ", mytree.postorder(mytree.root))
print("Binary: ", mytree.binarySearch(9))
print("DFS: ", mytree.dfs(9))
print("BFS: ", mytree.bfs(9))