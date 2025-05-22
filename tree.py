class Node:
    def __init__(self, data):
        self.data = data
        self.left = ''
        self.right = ''

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    def get_children(self):
        return self.left, self.right
    
    def set_left(self, new):
        self.left = new

    def set_right(self, new):
        self.right = new
    
    def __str__(self):
        return "Data: " + str(self.data) + ", Children: " + str(self.left) + ', ' + str(self.right)


class BinaryTree:

    def __init__(self, root_val):
        self.root = Node(root_val)

    def get_root(self):
        return self.root
    
    def add_node(self, data):
        # if greater go to right subtree
        if data > self.root.data:
            if self.root.right == '':
                self.root.right = Node(data)
            else:
                self.root.right.add_node(data)
        else:
            if self.root.left == '':
                self.root.left = Node(data)
            else:
                self.root.left.add_node(data)

bt = BinaryTree(1)