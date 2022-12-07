class Potential:
    ...
    
class CoulombPotential(Potential):
    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2

    def force(self, r):
        return (self.q1*self.q2)/r**2
