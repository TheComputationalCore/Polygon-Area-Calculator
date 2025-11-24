# 📐 Polygon Area Calculator

A modern, object-oriented Python utility for computing geometric properties of rectangles and squares — including area, perimeter, diagonal length, ASCII drawings, and shape packing calculations.  
Clean, simple, highly extensible, and fully documented.

---

## 🔖 Badges

![Tests](https://img.shields.io/badge/tests-passing-brightgreen?logo=pytest)
![Docs](https://img.shields.io/badge/docs-MkDocs%20Material-blue?logo=markdown)
![Deployed](https://img.shields.io/badge/deployed-GitHub%20Pages-brightgreen?logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features

### 🟦 Rectangle Class
- Compute **area**, **perimeter**, **diagonal**
- Generate ASCII pictures (`get_picture`)
- Measure how many shapes fit inside (`get_amount_inside`)
- Supports dynamic width & height updates
- Clean repr: `Rectangle(width=10, height=5)`

### 🟥 Square Class
- Inherits from `Rectangle`
- Always maintains equal sides
- Setter methods are overridden (`set_side`, `set_width`, `set_height`)
- Clean repr: `Square(side=5)`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/TheComputationalCore/Polygon-Area-Calculator.git
cd Polygon-Area-Calculator
pip install .
```

---

## 📘 Usage Example

```python
from polygon_calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())        # 50
print(rect.get_perimeter())   # 30
print(rect.get_diagonal())    # 11.18
print(rect.get_picture())

sq = Square(8)
print(sq.get_area())          # 64
sq.set_side(4)
print(sq.get_diagonal())      # 5.66
print(sq.get_picture())

rect.set_width(16)
rect.set_height(8)
print(rect.get_amount_inside(sq))  # 8
```

---

## 📊 Example Picture Output

```
**********
**********
**********
**********
**********
```

---

## 🖥️ Command Line Interface (CLI)

Run help:

```bash
polygon-calculator --help
```

Example:

```bash
polygon-calculator --rectangle 10 5
polygon-calculator --square 7
```

---

## 📚 Documentation

Full documentation is available at:

👉 https://thecomputationalcore.github.io/Polygon-Area-Calculator/

Documentation includes:

- Usage Guide  
- API Reference  
- CLI Guide  
- Examples  

---

## 🧪 Running Tests

```bash
pytest -q
```

---

## 🤝 Contributing

Contributions are welcome!  
See **CONTRIBUTING.md** for full workflow and guidelines.

---

## 🔐 Security

More details in **SECURITY.md**

---

## 📄 License

This project is licensed under the **MIT License**.


