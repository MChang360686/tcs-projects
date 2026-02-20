class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.children = []

    def get_value(self) -> int:
        return self.value
    
    def get_children(self) -> list | None:
        if len(self.children) > 0:
            return self.children
        else:
            return None
        
    def add_child(self, new_child: 'Node') -> None:
        self.children.append(new_child)

    def rem_child(self, child: 'Node') -> None:
        if child in self.get_children():
            self.children.remove(child)
        else:
            return None
        
    def __str__(self) -> str:
        return f'{self.value}'
    
class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.nodes = []
        self.height = 1

    def add_node(self, parent: Node, value: int) -> None:
        self.nodes.append(value)
        parent.add_child(Node(value))

    def delete_node(self, parent: Node, child: Node) -> None:
        parent.rem_child(child)
        
    def is_empty(self) -> bool:
        return True if self.root != None else False

    def bfs(self, curr: Node) -> None | list:
        if curr.get_children() == None:
            return
        else:
            return [ self.bfs(child) for child in curr.get_children() ]
        
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
n = Node(1)
n2 = Node(2)
n3 = Node(3)
t = Tree(5)



