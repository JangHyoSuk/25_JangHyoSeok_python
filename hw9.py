class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x}, {self.__y})')

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.left = Point(x1, y1)
        self.right = Point(x2, y2)

    def show(self):
        left_x, left_y = self.left.get()
        right_x, right_y = self.right.get()
        print(f'좌측 상단 꼭점이 ({left_x}, {left_y})이고 우측 하단 꼭지점이 ({right_x}, {right_y})인 사각형입니다.', end=' ')

    def getWidth(self):
        return self.right.get()[0] - self.left.get()[0]

    def getHeight(self):
        return self.right.get()[1] - self.left.get()[1]

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

