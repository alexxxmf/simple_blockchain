from datetime import datetime, timezone


class Block():
    """
    This is a simplified implementation of a bitcoin block
    model.
    """
    def init(self, prev_hash, hash, data):
        self.timestamp = datetime.now().replace(
            tzinfo=timezone.utc
        ).timestamp()
