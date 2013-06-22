from collections import deque

def makeSafe(node):
    if node == None: return ""
    else: return node.content

class Node:
    def __init__(self, x):
        self.content = x
        self.left = None
        self.right = None
    def __str__(self):
        return "/" + self.content + "/"
    
class Tree:
    def __init__(self):
        self.root = None
        
    def add(self, node, pivot):
        if pivot == None:
            self.root = node
        else:
            if pivot.content < node.content:
                if pivot.right == None:
                    pivot.right = node 
                else:
                    self.add(node, pivot.right)
            else:
                if pivot.left == None:
                    pivot.left = node 
                else:
                    self.add(node, pivot.left)
     
    def put(self, x):
        n = Node(x)
        self.add(n, self.root)
    
    def inorder(self, node):
        if node == None: return [];
        if node.left == None and node.right == None: 
            return [node.content]
        else:
            result = []
            result.extend(self.inorder(node.left))
            result.extend([node.content])
            result.extend(self.inorder(node.right))
            return result

    def postorder(self, node):
        if node == None: return [];
        if node.left == None and node.right == None: 
            return [node.content]
        else:
            result = []
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            result.extend([node.content])
            return result

    def preorder(self, node ):
        if node == None: return [];
        if node.left == None and node.right == None: 
            return [node.content]
        else:
            result = []
            result.extend([node.content])
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
            return result
        
    def bfs(self, nodeToSearch):
        visited = []        
        queue = deque([self.root])
        current = self.root
        path = [];
        
        while True:
            if queue == [] : return []
            if current.content == nodeToSearch:
                return [(x.content,makeSafe(x.left),makeSafe(x.right)) for x in path]            
            
            if current not in visited:
                for next in [current.left, current.right]:
                    if next!= None: queue.append(next)
                visited.append(current)
            current = queue.popleft()
            path.append(current);
            
    def dfs(self, nodeToSearch):
        visited=[]
        stack = [self.root]
        current = self.root
        path = []
        
        while True:
            if stack == [] : return []
            if current.content == nodeToSearch:
                return [(x.content,makeSafe(x.left),makeSafe(x.right)) for x in path]            
            if current not in visited:
                for next in [current.left, current.right]:
                    if next!= None: stack.append(next)
                visited.append(current)
            current = stack.pop()
            path.append(current)
            
    def binarySearch(self, nodeToSearch):
        current = self.root;
        path = [self.root]
        while True:
            if current.content == nodeToSearch:
                return [(x.content,makeSafe(x.left),makeSafe(x.right)) for x in path]
            next = None
            if nodeToSearch < current.content:
                if current.left != None: next = current.left
            else:
                if current.right != None: next = current.right
            if next==None: return []
            path.append(next)
            current = next;