from collections import namedtuple

# Stationary Store

Pen = namedtuple("Pen", "size inkcolor beveled")

ballpoint = Pen(1.3, "blue", True)
gel = Pen(.9, "green", False)
fountain = Pen._make([.3, "black", True])

for field, value in zip(ballpoint._fields, ballpoint):
    print(field, " = ", value)
print("----------------------")
for field, value in zip(gel._fields, gel):
    print(field, " = ", value)
print("----------------------")
for field, value in zip(fountain._fields, fountain):
    print(field, " = ", value)
print("----------------------")

# Slope of a Line

Point = namedtuple("Point", ["x", "y"])

p1 = Point._make([2, 1])
p2 = Point._make([4, 7])

def slope():
    return (p2.y - p1.y) / (p2.x - p1.x)

print(f'({p2.y} - {p1.y}) / ({p2.x} - {p1.x}) = slope = {slope()}')