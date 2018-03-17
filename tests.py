import unittest

from main import Block, Blockchain


class BlockTests(unittest.TestCase):
    """
    Tests for the Block object
    """
    def test_block_properties_are_properly_created(self):
        block = Block({'data': 'random'}, "0x1234")
        return self.fail(block)

if __name__ == "__main__":
    unittest.main()
