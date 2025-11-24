# 📚 API Reference

This page provides detailed documentation for all classes and methods in the **Polygon Area Calculator** project.

---

# 🟦 Rectangle

The `Rectangle` class represents a simple rectangle defined by its width and height.

## **Constructor**

```python
Rectangle(width, height)
```

### Parameters:
- **width** (`int` or `float`)
- **height** (`int` or `float`)

---

## **Methods**

### 🔹 `set_width(width)`
Sets a new width.

```python
rect.set_width(10)
```

### 🔹 `set_height(height)`
Sets a new height.

```python
rect.set_height(5)
```


### 🔹 `get_area()`
Returns the area of the rectangle.

```
width * height
```

```python
rect.get_area()
```

### 🔹 `get_perimeter()`
Returns the perimeter.

```
2 * width + 2 * height
```

```python
rect.get_perimeter()
```

### 🔹 `get_diagonal()`
Returns the diagonal length based on the Pythorean theorem.

```
(width² + height²) ** 0.5
```

```python
rect.get_diagonal()
```

### 🔹 `get_picture()`
Returns an ASCII-art representation of the rectangle using `*` characters.

- If width or height is greater than **50**, returns:
  ```
  Too big for picture.
  ```

```python
print(rect.get_picture())
```


### 🔹 `get_amount_inside(shape)`
Returns how many times another shape can fit inside the rectangle.

Measured using *integer* division:

```
(self.width // shape.width) * (self.height // shape.height)
```

```python
rect.get_amount_inside(sq)
```


### 🔹 `__str__()`
String representation of the rectangle:

```
Rectangle(width=10, height=5)
```

---

# 🟥 Square

The `Square` class is a subclass of `Rectangle`, where both width and height remain equal.

## **Constructor**

```python
Square(side)
```

### Parameter:
- **side** (`int` or `float`)

---

## **Methods**

### 🔹 `set_side(side)`
Sets both width and height to the same value.

```python
sq.set_side(6)
```

### 🔹 `set_width(width)` *(overridden)*
Ensures width and height remain equal.

### 🔹 `set_height(height)` *(overridden)*
Ensures width and height remain equal.

### 🔹 `__str__()`
String representation of a square:

```
Square(side=5)
```

---

# 🧱 Class Relationship Diagram

```
 Rectangle
    ▲
    │ (inherits)
    │
 Square
```

---

# 🧩 Notes

- All geometric calculations return numeric values.
- ASCII drawing uses `*` characters and line breaks.
- Shape packing always uses integer division.

---

You may now continue to **Examples** or **Usage** for practical demonstrations.
