class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.child = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def display(self):
        spaces = self.get_level() * ' '
        print(spaces + "|__"+str(self.val))
        if self.child:
            for children in self.child:
                children.display()


# node = TreeNode(10)
# child_node = TreeNode(3)
# child_node_2 = TreeNode(1)
# node.add_child(child_node)
# node.add_child(child_node_2)
# node.display()

"""BINARY SEARCH TREE"""

class BinaryTreeSearchTree:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None
    
    def add_child(self, data):
        if self.data == data:
            pass
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeSearchTree(data)
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeSearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        return elements 
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def find_closest(self, target):
        closest = 100000000
        current  = self
        while current is not None:
            if abs(closest - target) > abs(current.data - target):
                closest = current.data
            if target > closest:
                current = current.right
            elif target < closest:
                current = current.left
            else:
                break
        return closest
    




node = BinaryTreeSearchTree(20)
node.add_child(17)
node.add_child(4)
node.add_child(23)
node.add_child(18)
node.add_child(34)
node.add_child(22)
print(node.find_closest(3))
print(node.in_order_traversal())

        