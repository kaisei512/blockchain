import hashlib as hasher


class Block:
    
    def __init__(self,index,timestamp,data,previous_hash):
        
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8'))
        
        return sha.hexdigest()
    
if __name__=="__main__":
    
    import datetime as dt
    block = Block(1,dt.datetime.now(),"sample",0)
    print(block.index)