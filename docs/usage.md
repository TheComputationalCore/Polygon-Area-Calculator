# 📘 Usage Guide

This guide explains how to use the **Polygon Area Calculator** to work with rectangles and squares using Python.

---

## 🧱 Creating Shapes

### Rectangle
```python
from polygon_calculator import Rectangle

rect = Rectangle(10, 5)
```

### Square
```python
from polygon_calculator import Square

sq = Square(9)
```

Both classes store width and height internally.  
`Square` ensures both values always remain equal.

---

## ➕ Setting Dimensions

### Rectangle
```python
rect.set_width(12)
rect.set_height(4)
```

### Square
```python
sq.set_side(6)
# or
sq.set_width(6)
sq.set_height(6)
```

---

## 📐 Getting Measurements

### Area
```python
rect.get_area()      # width * height
sq.get_area()
```

### Perimeter
```python
rect.get_perimeter()
sq.get_perimeter()
```

### Diagonal
```python
rect.get_diagonal()
sq.get_diagonal()
```

---

## 🖼️ Generating Shape Pictures

You can generate ASCII-based visual representations:

```python
print(rect.get_picture())
```

Example output:

```
**********
**********
**********
```

Shapes larger than 50 in width or height return:

```
Too big for picture.
```

---

## 📦 Packing Shapes Inside Each Other

Determine how many times one shape fits inside another:

```python
rect = Rectangle(16, 8)
sq = Square(4)

rect.get_amount_inside(sq)   # returns 8
```

This calculates:

```
(rect.width // sq.width) * (rect.height // sq.height)
```

---

## 📄 String Representations

Each class has a descriptive `__str__`:

```python
print(Rectangle(3, 6))
# Rectangle(width=3, height=6)

print(Square(5))
# Square(side=5)
```

---

## 🧪 Next Steps

Explore:

- **API Reference** for full method descriptions  
- **Examples** for real-world usage  

Happy coding! 🚀
