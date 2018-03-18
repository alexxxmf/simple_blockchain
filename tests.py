import unittest

from main import Block, Blockchain, Transaction


class TansactionTests(unittest.TestCase):
    """
    Tests for the Transaction object
    """
    def setUp(self):
        self.tx = Transaction("Alex", "Alice", 50)

    def test_block_serialized(self):
        self.assertEqual(
            self.tx.serialized,
            {
                'from_address': 'Alex',
                'to_address': 'Alice',
                'amount': 50
            }
        )


class BlockTests(unittest.TestCase):
    """
    Tests for the Block object
    """
    def setUp(self):
        self.block = Block("random tx", "0x1234")

    def test_block_properties_are_properly_created(self):
        self.assertEqual(self.block.prev_hash, "0x1234")
        self.assertEqual(self.block.transaction, "random tx")
        self.assertIn("Block", str(self.block))

    def test_block_mine_method(self):
        difficulty = 1
        self.block.mine_block(1)
        self.assertEqual(self.block.hash[:difficulty], "0")

    def test_block_serialized(self):
        keys = ['transaction', 'nonce', 'timestamp', 'prev_hash', 'hash']
        # we change the way to test here because hash always changes for every
        # time we run the tests so we just check we have the same key structure
        for k in self.block.serialized:
            self.assertTrue(k in keys)


class BlockChainTests(unittest.TestCase):
    """
    Tests for the Block object
    """
    def setUp(self):
        self.blockchain = Blockchain()

    def test_blockchain_created_with_genesis(self):
        self.assertEqual(len(self.blockchain.chain), 1)

    def test_blockchain_mine_pending_tx(self):
        tx = Transaction("fromAlex", "toAlice", 50)
        self.blockchain.pending_transactions.append(tx)
        self.blockchain.mine_pending_transactions("0x1104")
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(len(self.blockchain.pending_transactions), 1)

    def test_blockchain_create_transaction(self):
        tx = Transaction("fromAlex", "toAlice", 50)
        self.blockchain.create_transaction(tx)
        self.assertEqual(len(self.blockchain.pending_transactions), 1)

    def test_blockchain_not_valid_when_block_is_modified(self):
        dummy_block = Block("random stuff", "0x00123")
        self.blockchain.chain.append(dummy_block)
        self.assertFalse(self.blockchain.check_if_chain_is_valid())

    def test_blockchain_get_address_balance(self):
        tx = Transaction("Alex", "Alice", 50)
        tx1 = Transaction("Alice", "Berto", 20)
        self.blockchain.create_transaction(tx)
        self.blockchain.create_transaction(tx1)
        self.blockchain.mine_pending_transactions("Mr.Miner")
        self.assertEqual(self.blockchain.get_address_balance("Alex"), -50)
        self.assertEqual(self.blockchain.get_address_balance("Mr.Miner"), 0)
        tx2 = Transaction("Alice", "Alex", 100)
        self.blockchain.create_transaction(tx2)
        self.blockchain.mine_pending_transactions("Mr.Miner")
        self.assertEqual(self.blockchain.get_address_balance("Alex"), 50)
        self.assertEqual(self.blockchain.get_address_balance("Mr.Miner"), 100)

if __name__ == "__main__":
    unittest.main()
