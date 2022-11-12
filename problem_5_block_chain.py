import hashlib
import time

class Block:
    def __init__(self, data, previous_hash = None, previous = None):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.previous = previous
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, block):
        if not block:
            return
        
        self.head = block
        self.size += 1
            
    def get_size(self):
        return self.size
    
    def get_blocks(self):
        block = self.head
        while block:
            yield block
            block = block.previous
            
    def has_record(self, data):
        if not self.head:
            return False
        
        block = self.head
        while block:
            if block.data == data:
                return True
            block = block.previous
            
        return False
        
    

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

def test(chain, data_to_find):
    print("size: {}".format(chain.get_size()))
    for block in chain.get_blocks():
        print("data:{} | hash:{} | timestamp:{} | previous_hash:{}".format(
            block.data, block.hash, block.timestamp, block.previous_hash))

    print("has {}? result:{}".format(data_to_find, chain.has_record(data_to_find)))
    print("has {}? result:{}".format("no-thing", chain.has_record("no-thing")))
    
data_to_find = "income:-20.0,current_blance:15.0,new_blance:-5.0"

# Test Case 1
block1 = Block("income:10.0,current_blance:5.0,new_blance:15.0")
block2 = Block("income:-20.0,current_blance:15.0,new_blance:-5.0", block1.hash, block1)

chain1 = BlockChain()
chain1.append(block1)
chain1.append(block2)

test(chain1, data_to_find)

# Test Case 2
chain2 = BlockChain()
test(chain2, data_to_find)

# Test Case 3
chain3 = BlockChain()
for i in range(10):
    data = "income:{},current_blance:{},new_blance:{}".format(10, 10 * i, 10 * i + 10)
    block = Block(data)
    chain3.append(block)
    i += 1
    
test(chain3, data)
