# from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

   # Insert the given value into the tree
    def insert(self, value):
       # check if the incoming value is less than the current node's value
        if value < self.value:
            # we know we need to go left
            # how do we know when we need to recurse again,
            # or when to stop?
            if not self.left:
                # we can park our value here
                self.left = BSTNode(value)
            else:
                # we can't park here
                # keep searching
                self.left.insert(value)
        else:
            # we know we need to go right
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


​  # Return True if the tree contains the value
# False if it does not
   def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)
​
   # Return the maximum value found in the tree
   def get_max(self):
        # we'll keep going right until there are no more nodes on the right side
        if not self.right:
            return self.value
        # otherwise, keep going right
        return self.right.get_max()
​
   def iterative_get_max(self):
        current_max = self.value
​
   current = self
    # traverse our structure
    while current is not None:
        if current.value > current_max:
            current_max = current.value
        # update our current_max variable if we see a larger value
        current = current.right
​
   return current_max
​
   # Call the function `fn` on the value of each node
    # Do we expect a return from the for_each function? No
   def for_each(self, fn):
    # call the fn on the value at this node
        fn(self.value)
​
        # pass this function to the left child
   if self.left:
        self.left.for_each(fn)
    # pass this function to the right child
    if self.right:
        self.right.for_each(fn)

​
   def iterative_for_each(self, fn):
        stack = []
​
       # add the root node
   stack.append(self)
​
    # loop so long as the stack still has elements
   while len(stack) > 0:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
​
   fn(current.value)
​
    # Depth-First traversal
    # LIFO ordering of the tree elements
​
#    def breadth_first_for_each(self, fn):
#         queue = deque()
# ​
#        # add the root node
#    queue.append(self)
# ​
#     # loop so long as the stack still has elements
#    while len(queue) > 0:
#         current = queue.popleft()
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
​
   fn(current.value)
​
​
​
v1 = random.randint(1, 101)
v2 = random.randint(1, 101)
v3 = random.randint(1, 101)
v4 = random.randint(1, 101)
v5 = random.randint(1, 101)
​
bst = BSTNode(5)
​
bst.insert(v1)
bst.insert(v2)
bst.insert(v3)
bst.insert(v4)
bst.insert(v5)
​
bst.for_each(lambda v: print(v))
