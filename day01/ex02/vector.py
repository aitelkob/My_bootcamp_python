import stdarray

class Vector:
    def __init__(self,values):
        self.values = []
        if isinstance(values,(list,int,tuple)) == False:
            raise ValueError("Vector Error")
        if isinstance(values,int) and a < 0:
            raise ValueError("empty")
        if isinstance(values,tuple) and ((len(a) != 2) or not all([isinstance(val,int) for val in values]) or (values[0] >= values [1])):
            raise ValueError("wrong format")


def main():
    xcoords = [1.0,2.0,3.0,4.0]
    ycoords = [5.0,8.0,6.0,9,0]

    x = Vector(xcoords)
    y = Vector(ycoords)
    print(x.coords, x.n)


if __name__ == '__main__':
    main()
