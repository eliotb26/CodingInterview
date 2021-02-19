#create Binary Search Tree and useful methods

#Notes: 
#       most nodes in param is BT.root

class Node: 
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree: 
    def __init__(self): 
        self.root = None

    def __repr__(self): 
        pass
        #

    def __str__(self): 
        pass
        #str uses the repr 

    def insert(self, node, data): 
        if self.root is None: 
            self.root = Node(data)

        elif data < node.data: 
            if node.left is None: 
                node.left = Node(data)
            else: 
                self.insert(node.left, data)
        elif data > node.data: 
            if node.right is None: 
                node.right = Node(data)
            else: 
                self.insert(node.right, data)

    def find(self, node, data): 
        if self.root is None:
            return None

        if node.data == data: #when equal 
            return node
        elif node.data > data: 
            if node.left: 
                self.find(node.left, data)
            else: return None
        elif node.data < data: 
            if node.right: 
                self.find(node.left, data)
            else: return None

    def minValueNode(self, node): 
        #find the smallest data node from the root given 
        current = node
        while (current.left is not None): 
            current = current.left
        return current.data

    def Delete(self, node, data): 
        #given the BST and the data to search for, 
        #this will delete the node with that data, and return the new 
        #data at that point
        if self.root is None: 
            return self.root
        
        if node.data > data: 
            #then node in the left subtree
            self.Delete(node.left, data)

        elif node.data < data: 
            #then node is in the right subtree
            self.Delete(node.right, data)

        #found the node to delete
        else:
            # print("found it", node.data)
            # if node.left is None and node.right is None:
            #     #if leaf node (no children)
            #     node.data = None
            #     node = None
            #     return None

            if node.left is None:
                #has right children
                temp = node.right
                node.data = None
                node = None
                return temp

            elif node.right is None: 
                #has left children 
                temp = node.left
                node.data = None 
                node = None
                return temp 

            #Node with two children
            #Algo -> replace with the min of the right subtree
            else: 
                temp = minValueNode(node.right)

                node.data = temp.data
                #delete from right subtree the node the just replaced 
                node.right = Delete(node.right, temp.data)

        return node.data

    def printTreeInOrder(self, node): 
        if (node!= None): 
            self.printTreeInOrder(node.left)
            print(node.data)
            self.printTreeInOrder(node.right)


def main(): 
    BT = BinaryTree()
    BT.insert(BT.root, 10)
    BT.insert(BT.root, 12)
    BT.insert(BT.root, 11)
    BT.insert(BT.root, 9)
    BT.insert(BT.root, 9)
    BT.insert(BT.root, 14)
    BT.insert(BT.root, 15)
    BT.printTreeInOrder(BT.root)
    print() 

    print("Structure")
    print(BT.root.data)
    print(BT.root.left.data)
    print(BT.root.right.data)
    print(BT.root.right.right.data)
    print(BT.root.right.left.data)
    
    BT.printTreeInOrder(BT.root)

    print("Root:", BT.root.data)

    print("deleted:", BT.Delete(BT.root, 14))       #TODO 
    print()
    BT.printTreeInOrder(BT.root)

    # node_val = BT.find(BT.root, 10).data
    # print("\n Found Node", node_val)

    # min_val = BT.minValueNode(BT.root)
    # print("\n Min Value: ", min_val)

    #TODO reorganize tree to have min length 
    
main()
