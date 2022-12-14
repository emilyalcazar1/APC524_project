import abc
import dataclasses

@dataclasses.dataclass
class Potential:
    @abc.abstractmethod
    def force(self, r):
        pass
    
class CoulombPotential(Potential):
    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2

    def force(self, r):
        return (self.q1*self.q2)/r**2

class InvPolyPotential(Potential):
    def __init__ (self, q1, q2, powers):
        self.q1 = q1
        self.q2 = q2
        self.powers = powers
            
    def force(self,r):
        pot = 0;
        for i in range(len(self.powers)):
            pot += self.powers[i]/r**i
        return (self.q1*self.q2)* pot
