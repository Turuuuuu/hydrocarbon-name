from dataclasses import dataclass

@dataclass
class Molecule:
    symbol: str
    count: int 
    
    def __init__(self, symbol: str, count: int):
        self.symbol = symbol
        self.count = count