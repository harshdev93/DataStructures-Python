class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

# All Add functions:
    def addToStart(self, data):
        # create a temporary node
        tempNode = Node(data)
        tempNode.next = self.head
        self.head = tempNode

    def addToEnd(self,data):
        tempNode = Node(data)
        curr = self.head
        while curr.next!= None:
            curr = curr.next
        curr.next = tempNode

    def addInMid(self,data,pos):
        count = 0
        temp = Node(data)
        curr = self.head
        while curr.next != None:
            print("out")
            print(type(pos), count, pos)
            if count != pos:
                curr = curr.next
                count = count + 1
                print(count)
                print("in")
            else:
                temp.next = curr.next
                curr.next = temp
                print("else")
                break

# All Delete Functions:
    def delFirst(self):
        self.head = self.head.next

    def delLast(self):
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None

    def delMid(self,pos):
        curr = self.head
        count = 0
        prev = None
        while curr.next != None:
            if count != pos:
                prev = curr
                curr = curr.next
                count = count + 1
            else:
                prev.next = curr.next
                break

# Methods to do, sort,

# Extra functions:
    def findDataAtPos(self,data):
        curr = self.head
        count = 0
        while curr.next != None:
            if curr.data == data:
                print("Data is present at position", count)
                break
            else:
                count = count + 1
                curr = curr.next

    def reverse(self):
        curr = self.head
        prev = None
        nextone = None
        while curr != None:
            nextone = curr.next
            curr.next = prev
            prev = curr
            curr = nextone
        self.head = prev

    def findMax(self):
        curr = self.head
        temp_max = 0
        while curr != None:
            if int(curr.data) > temp_max:
                temp_max = curr.data
                curr = curr.next
            else:
                curr = curr.next
        print(temp_max)

    def updateInPos(self,pos,data):
        curr = self.head
        count = 0
        while curr != None:
            if count == pos:
                curr.data = data
                break
            else:
                curr = curr.next
                count = count + 1

    def removeDuplicates(self):
        curr = self.head
        print(curr.data)
        d = {}
        print("Stage 1 starting")
        while curr != None:
            if curr.data not in d:
                d[curr.data] = 1
                curr = curr.next
            else:
                d[curr.data] = d[curr.data] + 1
                curr = curr.next
        count = 0
        prev = None
        print(d)
        print("stage 1 complete")
        curr = self.head
        while curr != None:
            if curr.data in d:
                if d[curr.data] == 1:
                    prev = curr
                    curr = curr.next
                    count = count + 1
                    continue
                elif d[curr.data] > 1:
                    if count == 0:
                        prev = curr
                        count = count + 1
                        curr = curr.next
                        continue
                    else:
                        d[curr.data] = d[curr.data] - 1
                        count = count + 1
                        prev.next = curr.next
                        curr = curr.next
        print("Stage 2 complete")

    def checkForPalindrome(self):
        curr = self.head
        self.reverse()
        curr1 = self.head
        while curr != None:
            if curr1.data == curr.data:
                curr1 = curr1.next
                curr = curr.next
                continue
            else:
                print("Not Palindrome")
        print("Palindrome")

    def sortLinked(self):
        curr = self.head
        while curr.next != None:
            curr1 = curr
            smallest = curr.data
            while curr1 != None:
                temp = curr.data
                if smallest <= curr1.data:
                    if curr1.next == None:
                        break
                    else:
                        curr1 = curr1.next
                        continue
                else:
                    smallest = curr1.data
                    curr.data = smallest
                    curr1.data = temp
                    if curr1.next == None:
                        break
                    else:
                        curr1 = curr1.next
                        continue

            curr = curr.next

    def mergeSorted(self,list2):
        curr = self.head
        curr1 = list2.head

        mylist3 = LinkedList()
        #print(curr1.data)

        while curr != None:
            if curr.data > curr1.data:
                # print("check1")
                if mylist3.head == None:
                    mylist3.addToStart(curr1.data)
                    if curr1.next != None:
                        curr1 = curr1.next
                        continue
                    else:
                        break
                else:
                    mylist3.addToEnd(curr1.data)
                    if curr1.next != None:
                        curr1 = curr1.next
                        continue
                    else:
                        break
                    # mylist3.display()
                    # continue
            elif curr1.data > curr.data:
                # print("check2")
                if mylist3.head == None:
                    mylist3.addToStart(curr.data)
                    if curr.next != None:
                        curr = curr.next
                        continue
                    else:
                        break
                else:
                    mylist3.addToEnd(curr.data)
                    if curr.next != None:
                        curr = curr.next
                        continue
                    else:
                        break
            else:
                # print("check3")
                if mylist3.head == None:
                    mylist3.addToStart(curr.data)
                    mylist3.addToEnd(curr1.data)
                    if curr1.next != None and curr.next != None:
                        curr1 = curr1.next
                        curr = curr.next
                        continue
                    else:
                        break
                else:
                    mylist3.addToEnd(curr.data)
                    mylist3.addToEnd(curr1.data)
                    if curr1.next != None and curr.next != None:
                        curr1 = curr1.next
                        curr = curr.next
                        continue
                    else:
                        break

        if curr1.next == None:
            curr3 = mylist3.head
            while curr3.next != None:
                curr3 = curr3.next
            if curr.next != None:
                curr3.next = curr
            # mylist3.display()
        if curr.next == None:
            curr3 = mylist3.head
            while curr3.next != None:
                curr3 = curr3.next
            if curr1.next != None:
                curr3.next = curr1
        mylist3.display()


    def N_after_M_Nodes(self,m,n):
        curr = self.head
        count = 0
        while curr.next != None:
            if count != m-1:
                print("check")
                count = count + 1
                curr = curr.next
            if count == m-1:
                print("check2")
                curr1 = curr
                if curr1.next == None:
                    print("check4")
                    break
                else:
                    print("check3")
                    count1 = n
                    while count1 > 0 and curr1.next != None: # curr1.next != None is added to check for a cae when say N = 2 but only one element is left in the end to be removed.
                        curr1 = curr1.next
                        count1 = count1 - 1
                    curr.next = curr1.next
                    count = -1  # updated to -1 and not 0 since for the first iteration curr needs to it moves 2 times and for the next iteration curr needs to move 3 time since curr is already at 1 (at head) in first iteration.
                    self.display()
                    continue

# Display Function:
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False
        while start!=None:
            print(str(start.data), end=" ")
            start = start.next
            if start:
                print("-->", end=" ")
        print()


myList = LinkedList()
myList2 = LinkedList()

# adding some elements to the start of LinkedList
# myList.addToStart(4)
# # myList.addToEnd(8)
# # myList.addToEnd(20)
# # myList.addToEnd(21)
#
# myList2.addToStart(4)
# myList2.addToEnd(11)
# myList2.addToEnd(15)
# myList2.addToEnd(17)

#myList.addToEnd(5)

# myList.mergeSorted(myList2)

#myList.addInMid("yo", int(1))
#myList.delFirst()
# myList.display()
#
# #myList.findDataAtPos("yo")
# #myList.display()
#
# #myList.delLast()
# #myList.delMid(1)
#
# #print("Reverse:")
# #myList.reverse()
# #
# # #myList.findMax()
# # #myList.display()
# #
# # #myList.updateInPos(2,10)
# # #myList.display()
# #
# # print("Before removing duplicates")
# # myList.display()
# #
# #print("After removing duplicates")
# #myList.checkForPalindrome()
# #myList.removeDuplicates()
#
# # print("After sorting")
# # myList.sortLinked()
# myList.display()


# adding some elements to the start of LinkedList
myList.addToStart(1)
myList.addToEnd(2)
myList.addToEnd(3)
myList.addToEnd(4)
myList.addToEnd(5)
myList.addToEnd(6)
myList.addToEnd(7)
myList.addToEnd(8)
myList.addToEnd(9)
myList.N_after_M_Nodes(3,2)
myList.display()


# myList2.addToStart(4)
# myList2.addToEnd(11)
# myList2.addToEnd(15)
# myList2.addToEnd(17)

