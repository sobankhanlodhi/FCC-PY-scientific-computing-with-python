class Rectangle:

        def __init__(self, width, height):
            self.width = width
            self.height = height

        def __str__(self):
            return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) +")"
        
        def set_width (self,width):
            self.width = width

        def set_height (self,height):
            self.height = height
        
        #get_area: Returns area (width * height)
        def get_area (self):
            return (self.width * self.height)

        #get_perimeter: Returns perimeter (2 * width + 2 * height)
        def get_perimeter(self):
            return (2 * self.width + 2 * self.height)

        #get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
        def get_diagonal(self):
            return ((self.width ** 2 + self.height ** 2) ** .5)

        #get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
        def get_picture(self):
            picture = ""
            if self.width > 50 or self.height > 50:
                return "Too big for picture."
            else:
                for loop in range(self.height):
                    picture = picture + ("*" * self.width) + "\n"
                return picture

        #get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        def get_amount_inside(self,shape):
            amount = int(self.width / shape.width) * int(self.height / shape.height)
            return amount

class Square(Rectangle):
    
    def __init__(self,side):
        self.width = side
        self.height = side

    def __str__(self):
        return ("Square(side=" + str(self.width) + ")")

    def set_side(self,side):
        self.width = side
        self.height = side