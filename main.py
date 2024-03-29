class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        w_asterisk = self.width * '*'
        picture = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                picture = picture + f"{w_asterisk}\n"

            return picture
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        area_1 = self.width * self.height
        area_2 = shape.width * shape.height

        n = area_1//area_2
        return n

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length

        super().__init__(width=self.side_length, height=self.side_length)

    def set_side(self, length):
        self.side_length = length
        self.width = length
        self.height = length

    def __str__(self):
        return f"Square(side={self.side_length})"

    def set_width(self, width):
        self.side_length = width

    def set_height(self, height):
        self.side_length = height
