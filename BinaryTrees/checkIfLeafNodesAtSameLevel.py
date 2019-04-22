import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def checkLeaf(root):
    q = queue.Queue()
    q.put(root)

    level = 0

    res = False
    while q.empty() != True:

        i = 0
        x = q.qsize()
        lcount = 0  # Leaf node count
        ncount = 0  # normal node count

        while i < x:
            # print("in")
            temp = q.get()
            if temp.left == None and temp.right == None:
                # print("l")
                lcount = lcount + 1
            else:
                # print("n")
                ncount = ncount + 1
                if temp.left != None:
                    q.put(temp.left)

                if temp.right != None:
                    q.put(temp.right)
            i = i + 1

        if lcount > 0 and ncount != 0:
            res = False
            break
        else:
            res = True
            continue

    print(res)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)


    checkLeaf(root)
