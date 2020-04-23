import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        # if value is greater than root
        else:
            if self.right:
                self.right.insert(value)
                # if right does not exist make it the first right.
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            # recursion on right pointer because values are greater
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
             # invoke the callback with the root value in params
            cb(self.value)
             #if there's a left node, utilize recursion to callback the values
            if self.left:
                self.left.for_each(cb)
            #same approach for the right side
            if self.right:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        ## utilize queue
        #initialize the queue
        q = Queue()

        #dequeue the node
        q.enqueue(node)

        while q.len() > 0:
            # current node is being removed
            current_node = q.dequeue()
            #print the value
            print(current_node.value)

            if current_node.left:
                # if the node has a left reference
                q.enqueue(current_node.left)
            if current_node.right:
                #same thing as left
                q.enqueue(current_node.right)





    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use stack when implementing depth
        stack = Stack()
        stack.push(node)
        # while the stack has a node
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)
            # check that left nodes exist. if true, then push the value(s)
            if current_node.left:
                stack.push(current_node.left)
            # same approach to the right side
            if current_node.right:
                stack.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    #Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
