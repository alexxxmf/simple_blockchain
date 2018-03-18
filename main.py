import time
import hashlib
import pickledb


class Transaction:
    """
    This model represents in a simplified way a transaction
    """
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount

    @property
    def serialized(self):
        return {
            'from_address': self.from_address,
            'to_address': self.to_address,
            'amount': self.amount
        }


class Block:
    """
    This is a simplified implementation of a bitcoin block
    model.
    Here a explanation what is the nonce property:
    https://en.bitcoin.it/wiki/Nonce
    """
    def __init__(self, transaction, prev_hash):
        self.timestamp = time.time()
        self.transaction = transaction
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.hash_block()

    def hash_block(self):
        concatenation = (
            str(self.prev_hash).encode('utf-8') +
            str(self.transaction).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.nonce).encode('utf-8')
        )
        return hashlib.sha256(concatenation).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.hash_block()

    @property
    def serialized(self):
        return {
            'timestamp': self.timestamp,
            'transaction': self.transaction,
            'prev_hash': self.prev_hash,
            'nonce': self.nonce,
            'hash': self.hash,
        }

    def __repr__(self):
        return "<Block {0}>".format(self.hash)


class Blockchain:
    """
    This is a simplified implementation of a blockchain. In this case,
    it will just consist of an ordered secuence of blocks.
    """
    def __init__(self):
        self.chain = []
        self.difficulty = 1
        self._create_genesis_block()
        self.pending_transactions = []
        self.mining_reward = 100

    def _create_genesis_block(self):
        """
        In every blockchain we need a Genesis Block, this is the function
        that creates it.
        """
        tx_zero = Transaction("", "", 0)
        genesis_block = Block([tx_zero, ], 0)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        previous_block = self.get_latest_block()
        block = Block(self.pending_transactions, previous_block)
        block.mine_block(self.difficulty)
        self.chain.append(block)

        miner_reward = Transaction("", miner_address, self.mining_reward)
        self.pending_transactions = [miner_reward]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_address_balance(self, address):
        balance = 0
        for block in self.chain:
            for individual_transaction in block.transaction:
                if individual_transaction.from_address == address:
                    balance -= individual_transaction.amount
                if individual_transaction.to_address == address:
                    balance += individual_transaction.amount
        return balance

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

            return True

    @property
    def config_serialized(self):
        # Here we ommit chain property because it will be what we are going
        # to store in a separate db, this will go into a blockchain config db
        return {
            'difficulty': self.difficulty,
            'pending_transactions': self.pending_transactions,
            'mining_reward': self.mining_reward,
        }
