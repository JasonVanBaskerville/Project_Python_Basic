class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return ((self.width)**2 + (self.height)**2)** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        teks = ""
        for i in range(self.height):
            teks += f"{'*' * self.width}\n"
        return teks
    
    def get_amount_inside(self, shape):
        horizontal = self.width // shape.width
        vertical = self.height // shape.height
        return horizontal * vertical

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
 

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
    
    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


    # =========================
# TEST RECTANGLE
# =========================

rectangle = Rectangle(4, 8)

print("=== Rectangle ===")

print("Width:", rectangle.width)
print("Height:", rectangle.height)

print("Area:", rectangle.get_area())
print("Perimeter:", rectangle.get_perimeter())
print("Diagonal:", rectangle.get_diagonal())

print("Picture:")
print(rectangle.get_picture())

print("String:", rectangle)


# =========================
# TEST SET WIDTH & HEIGHT
# =========================

rectangle.set_width(10)
print("After set_width(10):", rectangle)

rectangle.set_height(5)
print("After set_height(5):", rectangle)


# =========================
# TEST AMOUNT INSIDE
# =========================

rectangle = Rectangle(4, 8)
square = Square(4)

print("\n=== Amount Inside ===")
print("Rectangle:", rectangle)
print("Square:", square)
print("Amount:", rectangle.get_amount_inside(square))


# =========================
# TEST SQUARE
# =========================

square = Square(5)

print("\n=== Square ===")

print("Width:", square.width)
print("Height:", square.height)

print("Area:", square.get_area())
print("Perimeter:", square.get_perimeter())
print("Diagonal:", square.get_diagonal())

print("String:", square)


# =========================
# TEST SQUARE SETTERS
# =========================

square.set_width(10)
print("After set_width(10):", square)

square.set_height(7)
print("After set_height(7):", square)

square.set_side(3)
print("After set_side(3):", square)