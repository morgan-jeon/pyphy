from .vector import vector

class object:
    def __init__(self):
        self.mass = 1.0
        self.charge = 0
        self.pos = vector(0,0)
        self.v = vector(0,0)
        self.a = vector(0,0)
        self.force = vector(0,0)

    def __repr__(self):
        prop = {}
        prop['mass'] = self.mass
        if self.charge != 0:
            prop['charge'] = self.charge

        return f'Object({", ".join([f"{i}={prop[i]}" for i in prop])})'

    def update(self, timeInterval: int=1):
        self.a = self.force / self.mass
        self.v += self.a * timeInterval
        self.pos += self.v * timeInterval
        self.a *= 0