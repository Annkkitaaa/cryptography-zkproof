import numpy as np
import hashlib
from typing import List
from dataclasses import dataclass

@dataclass
class ZKProof:
    commitment: str
    challenge: int
    response: List[int]

class ZKProofSystem:
    def __init__(self, secret_numbers: List[int], modulus: int = 23):
        self.secret = secret_numbers
        self.modulus = modulus

    def generate_random_numbers(self, size: int) -> List[int]:
        return [np.random.randint(1, self.modulus) for _ in range(size)]
    
    def create_commitment(self, random_values: List[int]) -> str:
        commitment_input = ''.join(map(str, random_values))
        return hashlib.sha256(commitment_input.encode()).hexdigest()
    
    def generate_challenge(self) -> int:
        return np.random.randint(0, 2)
    
    def generate_response(self, random_values: List[int], challenge: int) -> List[int]:
        if challenge == 0:
            return random_values
        return [(r + s) % self.modulus for r, s in zip(random_values, self.secret)]
    
    def verify_proof(self, proof: ZKProof, public_sum: int) -> bool:
        response_sum = sum(proof.response) % self.modulus
        
        if proof.challenge == 0:
            commitment_check = self.create_commitment(proof.response)
            return commitment_check == proof.commitment
        return response_sum == public_sum
