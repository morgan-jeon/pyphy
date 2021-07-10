import math

class vector:
    def __init__(self, x, y):
        self.x, self.y = map(float, (x, y))

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        nx = self.x + other.x
        ny = self.y + other.y
        return vector(nx, ny)
    
    def __sub__(self, other):
        nx = self.x - other.x
        ny = self.y - other.y
        return vector(nx, ny)
    
    def __mul__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            return vector(self.x * other, self.y * other)
        elif(isinstance(other, vector)):
            return self.x * other.x + self.y * other.y
        else:
            raise ValueError('Multipies not declared')

    def __matmul__(self, other):
        if(isinstance(other, vector)):
            return self.x * other.y - self.y * other.x
        else:
            raise ValueError('Multipies not declared')

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            return vector(self.x/other, self.y/other)
        else:
            raise ValueError('Division not declared')

    def __neg__(self):
        return self * -1

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)
        
    def __ne__(self, other):
        return abs(self) != abs(other)

    def normalized(self):
        # Counter Clockwise
        return vector(self.x, self.y)/abs(self)

    def norm(self):
        return vector(-self.y, self.x)

    def rotated(self, angle):
        x = self.x*math.cos(angle)-self.y*math.sin(angle)
        y = self.x*math.sin(angle)+self.y*math.cos(angle)
        return vector(x,y)