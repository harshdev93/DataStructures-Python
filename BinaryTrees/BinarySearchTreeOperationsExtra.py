# Binary search tree operation:
# 1.TopView
# 2.BottomView

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0

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

    # Top View
    def topView(self, x):
        queueL = []
        dict_d = {}

        dict_d[0] = x.data
        queueL.append(x)

        while len(queueL) != 0:
            temp = queueL.pop(0)
            if temp.hd not in dict_d:
                dict_d[temp.hd] = temp.data


            if temp.left != None:
                queueL.append(temp.left)
                temp.left.hd = temp.hd - 1

            if temp.right != None:
                queueL.append(temp.right)
                temp.right.hd = temp.hd + 1
                # print("right", temp.data, temp.hd, temp.right.data, temp.right.hd)

        for i in sorted(dict_d.values()):
            print(i)

    # Bottom View
    def bottomView(self,x):
        queueL = []
        dict_d = {}

        dict_d[0] = [x.data]
        queueL.append(x)


        while len(queueL) != 0:
            temp = queueL.pop(0)

            if temp.left != None:
                queueL.append(temp.left)
                temp.left.hd = temp.hd - 1

                if temp.left.hd not in dict_d:
                    dict_d[temp.left.hd] = [temp.left.data]
                else:
                    dict_d[temp.left.hd].append(temp.left.data)
            if temp.right != None:
                queueL.append(temp.right)
                temp.right.hd = temp.hd + 1

                if temp.right.hd not in dict_d:
                    dict_d[temp.right.hd] = [temp.right.data]
                else:
                    dict_d[temp.right.hd].append(temp.right.data)

        for i in sorted(dict_d): # sorting the keys
            print(dict_d[i][-1])


tree = Tree()
# arr = [8,3,1,6,4,7,10,14,13]

# arr = [4, 2, 5, 1, 3]
# arr = [4, 2, 5, 1, 3]
arr = [15,5,8,6,24,19,30,21,9]

for i in arr:
    tree.insert(i)

print("Printing top view")
tree.topView(tree.root)

print("Printing bottom view")
tree.bottomView(tree.root)


# References:
# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
# https://www.geeksforgeeks.org/bottom-view-binary-tree/
