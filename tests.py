import unittest

from main import Block, Blockchain


class BlockTests(unittest.TestCase):
    """
    Tests for the Block object
    """
    def test_block_properties_are_properly_created(self):
        block = Block("random data", "0x1234")
        self.assertEqual(block.prev_hash, "0x1234")
        self.assertEqual(block.data, "random data")
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

    def test_blockchain_new_block(self):
        self.blockchain.create_new_block("random stuff")
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(
            self.blockchain.chain[-1].prev_hash,
            self.blockchain.chain[-2].hash
        )

    def test_blockchain_get_latest_block(self):
        self.blockchain.create_new_block("random stuff")
        block = self.blockchain.get_latest_block()
        self.assertEqual(block.data, "random stuff")

    def test_blockchain_not_valid_when_block_is_modified(self):
        dummy_block = Block("random stuff", "0x00123")
        self.blockchain.chain.append(dummy_block)
        self.assertFalse(self.blockchain.check_if_chain_is_valid())

if __name__ == "__main__":
    unittest.main()
