class BinarySearchTreeNode():
    # This part is used to create instance object
    # It basicall automatically creates properties that all object will take
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    # This is a method for adding or reading a data 
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # Add data to the left subtree
            if self.left:
                self.left.add_child( data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Add data to the right subtree
            if self.right:
                self.right.add_child( data)
            else:
                self.right = BinarySearchTreeNode(data)
    

    # This method is checking if the value that has been passed on the function is in the binary tree
    def search(self, val):
        # If the first data matches the one you are finding, it will simply return true
        if self.data == val:
            return True
        
        # However, we need a recurssion to simply rerunning the search method in order 
        # to find the whether the value is in the data
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
       
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


    # This method is created to sort data according to its order
    # The root value is in the middle of right tree and left tree
    def in_order_traversal(self):
        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit Base node
        elements.append(self.data)

        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # Method for finding the minimum and maximum value among the given elements
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data


    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    

    # Pre order Traversal 
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    # Post order traversal
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            elif val > self.data:
                if self.right:
                    self = self.right(val)
            else:
                if self.left is None and self.right is None:
                    return None
                if self.left is None:
                    return self.right
                if self.right is None:
                    return self.left
                
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
        
        return self