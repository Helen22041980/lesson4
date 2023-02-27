class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.wigth = abs(x1-x2)
        self.height=abs(y1 - y2)

    def perimetr(self):
        return 2 * (self.height + self.wigth)



a = Rectangle(1, 2, 5, 6)
print(a.perimetr())

