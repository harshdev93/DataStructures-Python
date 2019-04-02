class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)

        else:
            curr = self.root
            while 1:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    else:
                        curr = curr.left
                elif data > curr.data:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    else:
                        curr = curr.right

    # V-L-R
    def preorder(self,x):

        if x is not None:
            print(x.data)
            self.preorder(x.left)
            self.preorder(x.right)

    # L-V-R
    def inorder(self,x):

        if x is not None:
            self.inorder(x.left)
            print(x.data)
            self.inorder(x.right)

    # L-R-V
    def postorder(self,x):

        if x is not None:
            self.postorder(x.left)
            self.postorder(x.right)
            print(x.data)

    def modifiedInorder(self,x,temp):

        print("We are in modified Inorder")
        if x is not None:
            self.modifiedInorder(x.left,temp)

            print(x.data)
            temp.append(x.data)

            self.modifiedInorder(x.right,temp)
        # print("List is", temp)
        return temp

    def searchForSuccessor(self, curr):
        temp = []
        z = self.modifiedInorder(self.root,temp)
        # print(z)
        # print(z.index(curr.data))
        y = z[z.index(curr.data) + 1]
        successor = y
        # print(successor)
        self.delete(successor)
        curr.data = successor


    def delete(self,key):

        # first search
        if self.root is None:
            print("Not found")
        curr = self.root

        while curr.data != key and curr is not None:

            # print("Enter")

            parent = curr

            if curr is None:
                return ("Key not present")
            if curr.data == key:
                print("Found")
                break

            elif key < curr.data:

                curr = curr.left
                continue

            elif key > curr.data:

                curr = curr.right
                continue
        # print(curr.data)

        # if curr is a leaf node
        if curr.left is None and curr.right is None:
            if curr.data > parent.data:
                parent.right = None
            else:
                parent.left = None
            return
            # break

        # if curr has right child only
        elif curr.left is None:
            temp = curr.right.data
            curr.data = temp
            curr.right = None
            # break

        # if curr has left child only
        elif curr.right is None:
            temp = curr.left.data
            curr.data = temp
            curr.left = None
            # break



        # when the node to be deleted is a node having both left and right subtree
        # replace the node to be deleted with the inorder successor
        elif curr.left != None and curr.right != None:
            self.searchForSuccessor(curr)
    
    def LevelOrderTraversal(self,x):
        s = queue.Queue()
        s.put(x)
        while s.empty() == False:
            node = s.get()
            print(node.data)
            if node.left != None:
                s.put(node.left)
            if node.right!= None:
                s.put(node.right)
    
    # ZigZag traversal right->left->right...
    def zigzag(self,x):
        #initialize 2 stacks
        s1 = []
        s2 = []
        curr = x
        s1.append(curr)
        while len(s1) != 0 or len(s2) != 0:
            while len(s1) != 0:
                temp = s1.pop()
                if temp.left != None:
                    s2.append(temp.left)
                if temp.right != None:
                    s2.append(temp.right)
                print(temp.data)
            while len(s2) != 0:
                temp = s2.pop()
                if temp.right != None:
                    s1.append(temp.right)
                if temp.left != None:
                    s1.append(temp.left)
                print(temp.data)

    # searching for a node
    def search(self,key):

        if self.root is None:
            print("Not found")

        curr = self.root


        while 1:
            if curr is None:
                print("Key not present")
                break
            if curr.data == key:
                print("Found")
                break
            elif key < curr.data:
                curr = curr.left
            elif key > curr.data:
                curr = curr.right

    # calculates height based in the number of nodes.
    # to calculate height based on the number of edges, return -1 is curr is None
    def heightOfBianrytree(self,x):

        curr = x
        if curr is None:
            return 0

        lheight = self.heightOfBianrytree(curr.left)
        rheight = self.heightOfBianrytree(curr.right)
        return max(lheight,rheight) + 1



tree = Tree()
# arr = [8,3,1,6,4,7,10,14,13]

# arr = [4, 2, 5, 1, 3]
# arr = [4, 2, 5, 1, 3]
arr = [15,5,8,6,24,19,30,21,9]

for i in arr:
    tree.insert(i)

# print("Printing preorder")
# tree.preorder(tree.root)
#
# print("Printing postorder")
# tree.postorder(tree.root)
#
print("Printing inorder")
tree.inorder(tree.root)
#
# print("search")
# tree.search(6)
#
# print("Height of the tree")
# print(tree.heightOfBianrytree(tree.root))

print("Deleting a node")
tree.delete(15)

tree.inorder(tree.root)

print("Level Order Traversal")
tree.LevelOrderTraversal(tree.root)

print("ZigZag Traversal")
tree.zigzag(tree.root)

# tree.search(3)
# tree.delete(3)



# References:
# https://www.geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/
# https://stackoverflow.com/questions/300935/are-duplicate-keys-allowed-in-the-definition-of-binary-search-trees
# https://gist.github.com/samidhtalsania/6659380
# https://www.youtube.com/watch?v=ZM-sV9zQPEs&t=519s
# https://docs.python.org/3/library/asyncio-queue.html
# https://www.youtube.com/watch?v=vjt5Y6-1KsQ
