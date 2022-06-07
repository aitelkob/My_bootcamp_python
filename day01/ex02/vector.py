import stdarray


class Vector:
    def __init__(self,values):
        self.values =values[:]
        self.n = len(values)
    
    def __getitem__(self,i):
        return self._coords[i]
    def __add__(self,other):
        result = stdarray.create1D(self.n,0)
        for i in range(self.n):
            result[i] = self.values[i] + other.values[i]
        return Vector(result)

def main():
    xcoords = [1.0,2.0,3.0,4.0]
    ycoords = [5.0,8.0,6.0,9,0]

    x = Vector(xcoords)
    y = Vector(ycoords)
    print(x.coords, x.n)


if __name__ == '__main__':
    main()
