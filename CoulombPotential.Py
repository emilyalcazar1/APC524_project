class Potential:
    ...
    
class CoulombPotential(Potential):
    q1: int
    q2: int
    r: int

    def force(q1, q2, r):
        return (q1*q2)/r**2
