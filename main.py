import time


class Block():
    """
    This is a simplified implementation of a bitcoin block
    model.
    """
    def init(self, prev_hash, hash, data):
        self.timestamp = time.time()
