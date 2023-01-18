class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
def linked_list_to_set(head):
    # Convert a linked list to a set
    result = set()
    node = head

    while node:
        result.add(node.value)
        node = node.next
    return result

def union(llist_1, llist_2):
    set1 = set()
    set2 = set()
    
    if llist_1 and llist_1.head:
        set1 = linked_list_to_set(llist_1.head)

    if llist_2 and llist_2.head:
        set2 = linked_list_to_set(llist_2.head)
        
    united_list = sorted(list(set1.union(set2)))
    
    linked_list = LinkedList()
    for i in united_list:
        linked_list.append(i)
    
    return linked_list
    

def intersection(llist_1, llist_2):
    set1 = set()
    set2 = set()
    
    if llist_1 and llist_1.head:
        set1 = linked_list_to_set(llist_1.head)

    if llist_2 and llist_2.head:
        set2 = linked_list_to_set(llist_2.head)
        
    intersections = set()
        
    for item in set1:
        if item in set2:
            intersections.add(item)
    
    linked_list = LinkedList()
    for i in intersections:
        linked_list.append(i)
    
    return linked_list
    

# Test case 1
print('test 1 -----------------')
"""
test 1 -----------------
1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 -> 
4 -> 21 -> 6 -> 
"""
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
print('test 2 -----------------')
"""
test 2 -----------------
1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 -> 

"""
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 3
"""
test 3 -----------------


"""
print('test 3 -----------------')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 4
"""
test 4 -----------------
1 -> 2 -> 3 -> 

"""
print('test 4 -----------------')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2,3]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 5
"""
test 5 -----------------
1 -> 2 -> 3 -> 

"""
print('test 5 -----------------')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,2,3]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 6
"""
test 6 -----------------
1 -> 2 -> 

"""
print('test 6 -----------------')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1]
element_2 = [2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 7
"""
test 7 -----------------
2 -> 3 -> 

"""
print('test 7 -----------------')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 3, 3, 3]
element_2 = [2, 2, 2, 2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))