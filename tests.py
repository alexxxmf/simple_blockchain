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

if __name__ == "__main__":
    unittest.main()
