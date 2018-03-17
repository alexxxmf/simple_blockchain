import time
import hashlib


class Block():
    """
    This is a simplified implementation of a bitcoin block
    model.
    """
    def init(self, data, prev_hash):
        self.timestamp = time.time()
        self.prev_hash = prev_hash
        self.current_hash = self.hash_block()
        self.data = data

    def hash_block(self):
        concatenation = (
            str(self.prev_hash) +
            str(self.data) +
            str(self.timestamp)
        )
        return hashlib.sha256(concatenation).hexdigest()


class Blockchain():
    """
    This is a simplified implementation of a blockchain. In this case,
    it will just consist of an ordered secuence of blocks.
    """
    def init(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block():
        """
        In every blockchain we need a Genesis Block, this is the function
        that creates it.
        """
        genesis_block = Block("Genesis Block", 0)
        return genesis_block
