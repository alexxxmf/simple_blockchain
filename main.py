import time
import hashlib


class Block:
    """
    This is a simplified implementation of a bitcoin block
    model.
    """
    def __init__(self, data, prev_hash):
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        concatenation = (
            str(self.prev_hash) +
            str(self.data) +
            str(self.timestamp)
        )
        return hashlib.sha256(concatenation).hexdigest()

    def __repr__(self):
        return "<Block {0}>".format(self.hash)


class Blockchain:
    """
    This is a simplified implementation of a blockchain. In this case,
    it will just consist of an ordered secuence of blocks.
    """
    def __init__(self):
        self.chain = []
        self._create_genesis_block()

    def _create_genesis_block(self):
        """
        In every blockchain we need a Genesis Block, this is the function
        that creates it.
        """
        genesis_block = Block("Genesis Block", 0)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def create_new_block(self, data):
        previous_block = self.get_latest_block()
        block = Block(previous_block.hash, data)
        self.chain.append(block)

    def check_if_chain_is_valid(self):
        for block in self.chain:
            if self.chain.index(block) == 0:
                continue
            current_block = block
            previous_block = self.chain[(self.chain.index(block) - 1)]

            if current_block.hash != current_block.hash_block():
                return False

            if current_block.prev_hash != previous_block.hash:
                return False
