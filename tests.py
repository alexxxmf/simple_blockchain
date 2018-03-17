import unittest

from main import Block, Blockchain, Transaction


class BlockTests(unittest.TestCase):
    """
    Tests for the Block object
    """
    def test_block_properties_are_properly_created(self):
        block = Block("random tx", "0x1234")
        self.assertEqual(block.prev_hash, "0x1234")
        self.assertEqual(block.transaction, "random tx")
        self.assertIn("Block", str(block))

    def test_block_mine_method(self):
        block = Block("random data", "0x1234")
        difficulty = 1
        block.mine_block(1)
        self.assertEqual(block.hash[:difficulty], "0")


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
