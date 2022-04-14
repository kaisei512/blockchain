from numpy import block
from genesis import *
from new_block import *
import time


blockchain = [create_genesis_block()]
previous_block = blockchain[0]


num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    
    blocks_to_add = next_block(previous_block)
    blockchain.append(blocks_to_add)
    previous_block = blocks_to_add
    
    time.sleep(2)
    print(f"Block {blocks_to_add.index} has been added to the blockchain!")
    print(f"Hash: {blocks_to_add.hash}\n")