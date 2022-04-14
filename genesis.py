from block import *
import datetime as dt

def create_genesis_block():
    
    # 一つ目のブロック生成
    return Block(0, dt.datetime.now(), 'Genesis Block', '0')


