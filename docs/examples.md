# 📘 Examples

This page contains complete examples demonstrating how to use the **Polygon Area Calculator** in real scenarios.

---

## 🧱 Example 1 — Basic Rectangle Usage

```python
from polygon_calculator import Rectangle

rect = Rectangle(10, 5)

print(rect.get_area())        # 50
print(rect.get_perimeter())   # 30
print(rect.get_diagonal())    # 11.18...
print(rect.get_picture())
```

**Output:**
```
**********
**********
**********
**********
**********
```

---

## 🟥 Example 2 — Working With Squares

```python
from polygon_calculator import Square

sq = Square(8)

print(sq.get_area())          # 64
sq.set_side(4)
print(sq.get_perimeter())     # 16
print(sq.get_picture())
```

**Output:**
```
****
****
****
****
```

---

## 🔄 Example 3 — Updating Dimensions

```python
rect = Rectangle(12, 6)

rect.set_width(20)
rect.set_height(4)

print(rect)  
# Rectangle(width=20, height=4)
```

---

## 📦 Example 4 — Fitting Shapes Inside Each Other

```python
rect = Rectangle(16, 8)
sq = Square(4)

print(rect.get_amount_inside(sq))   # 8
```

Explanation:

```
(16 // 4) * (8 // 4) = 4 * 2 = 8
```

---

## 🧩 Example 5 — Handling Too-Large Shapes for Pictures

```python
rect = Rectangle(60, 4)
print(rect.get_picture())
```

**Output:**
```
Too big for picture.
```

---

## 📚 Continue Exploring

- Read the **Usage Guide** for step-by-step instructions  
- Check the **API Reference** for method descriptions  

Happy coding! 🚀
