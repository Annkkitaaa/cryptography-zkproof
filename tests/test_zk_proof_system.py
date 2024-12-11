import unittest
from src.zk_proof_system import ZKProofSystem

class TestZKProofSystem(unittest.TestCase):
    def test_commitment(self):
        zk = ZKProofSystem([10, 20])
        random_values = [5, 7]
        commitment = zk.create_commitment(random_values)
        self.assertEqual(len(commitment), 64)  # SHA-256 hash length
        
    def test_response(self):
        zk = ZKProofSystem([10, 20])
        random_values = [5, 7]
        response = zk.generate_response(random_values, 1)
        self.assertEqual(len(response), len(random_values))
