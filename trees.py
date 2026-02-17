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
        
    def __str__(self) -> str:
        return f'{self.value}'
    
class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.height = 1

    def add_node(self, parent: Node, value: int) -> None:
        parent.children.append(Node(value))

    def delete_node(self, parent: Node, child: Node) -> str| None:
        if child in parent.get_children():
            parent.children.remove(child)
        else:
            return 'child does not exist'

t = Tree(2)
t.add_node(t.root, 5)
t.add_node(t.root.children[0], 8)
print(t.root, t.root.get_children())
print(t.root.children[0], t.root.children[0].get_children())
print(t.delete_node(t.root.children[0], t.root.children[0].children[0]))
print(t.root, t.root.get_children())
print(t.root.children[0], t.root.children[0].get_children())