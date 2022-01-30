# Creating Class
class Point:
    # Create method 1
    def move(self):
        print("move")

    # Create method 2
    def draw(self):
        print("draw")


# Create Object instance from Class
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
point2.y = 2
print(point2.x)
point2.draw()
