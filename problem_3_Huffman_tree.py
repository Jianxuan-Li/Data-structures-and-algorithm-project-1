import sys
import heapq

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.val)
    
    def __lt__(self, other):
        if type(other) is str:
            return False
        return (self.val < other)

    def __le__(self, other):
        if type(other) is str:
            return False
        return(self.val <= other)

    def __gt__(self, other):
        if type(other) is str:
            return True
        return(self.val > other)

    def __ge__(self, other):
        if type(other) is str:
            return True
        return(self.val >= other)
    
def make_huffman_code(node, binstr = ""):
    # break condition
    if not node:
        return {}
    
    # code of a char
    if type(node) is str:
        return {node: binstr}

    # find code by recusion to traverse the tree
    d = dict()
    d.update(make_huffman_code(node.left[1], binstr + '0'))
    d.update(make_huffman_code(node.right[1], binstr + '1'))
    return d

def huffman_encoding(data):
    if not data or not len(data):        
        return data, None
    
    # find frequency
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # create a heap to save the frequency
    heap = []
    for char in frequency:
        heapq.heappush(heap, (frequency[char], char))
        
    # only has one letter
    if len(heap) == 1:
        freq, char = heapq.heappop(heap)
        root = TreeNode(0)
        root.left = (56, char)
        code = b"0" * len(data)
        return bytes(code), root

    # create the tree by the heap
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        f = left[0] + right[0]
        root = TreeNode(f)
        root.left = left
        root.right = right
        heapq.heappush(heap, (f, root))
        
    root = heapq.heappop(heap)
    
    # create the huffman code string
    huffman_code = make_huffman_code(root[1])
    binstr = b""
    for char in data:
        binstr += bytes(huffman_code[char], "UTF-8")
            
    return binstr, root[1]

def huffman_decoding(data, tree):
    if not tree or not data:
        return data

    i = 0
    result = ""
    
    while i < len(data):
        node = tree
        while node:
            one_byte = data[i:i+1]
            if type(node) is str:
                result += node
                break
            
            if one_byte == b"0":
                node = node.left[1]
                i += 1
                continue
            
            elif one_byte == b"1":
                node = node.right[1]
                i += 1
                continue
                
    return result

if __name__ == "__main__":
    codes = {}

    def test(a_great_sentence):
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
        print ("----------")
        
    
    test("The bird is the word")
    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    test("ABCD")

    # Test Case 2
    test("AAAAAAABBBCCCCCCCDDEEEEEE")

    # Test Case 3
    test("AB")
    
    # Test Case 4
    test("DDDDEEEEBBBBB")
    
    # Test Case 5
    test("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    # Test Case 6
    test("a")
    
    # Test Case 8    
    test("0000")
