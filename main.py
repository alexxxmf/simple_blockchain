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
        concatenation = str(self.prev_hash) + str(self.data) + str(self.timestamp)
        hash = hashlib.sha256(concatenation).hexdigest()
        return hash
