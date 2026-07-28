from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        random_move = random.choice(self.moves)
        self.position = tuple(map(sum, zip(self.position, random_move)))
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0), (0,1), (-1,0), (0,-1)]
    def level_up(self):
        self.moves.extend([(1,1), (1,-1),(-1,1), (-1,-1)])
