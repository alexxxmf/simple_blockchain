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


class BlockChainTests(unittest.TestCase):
    """
    Tests for the Block object
    """
    def test_blockchain_created_with_genesis(self):
        blockchain = Blockchain()
        self.assertEqual(len(blockchain.chain), 1)

if __name__ == "__main__":
    unittest.main()
